import sys
import importlib

from utils import fetch_doc , save

# Parsing
class Parser:

    # Exclusively works with lists.
    # Actual parsing... too roundabout?
    def __parse__(self , doc , fields):
        output = []
        for field in fields:
            t_list = doc

            tag = None
            attrs = {"id" : "" , "class" : []}
            
            # Homing in...
            for t in field.split(" "):

                if t.startswith("#"):
                    attrs["id"] = t.replace("#" , "")
                
                elif t.startswith("."):
                    attrs["class"].insert(t.replace("." , ""))
                elif t[0].isalnum():
                    tag = t

            t_list = t_list.find_all(tag , attrs = attrs)

            for t in t_list:
                output.insert(len(output),t.text)
        
        return output

    def __field_util__(self , field):
        output = list(())
        ft = type(field)

        if ft == str:
            output.insert(len(output), field)
        elif ft == list or ft == tuple or ft == set:
            output = list(field)
        return output

    def parse(self , doc , fields):
        output = dict({})
        #tag-type
        tt = type(fields)

        if tt == dict:
            for field in fields:
                output[field] = self.__parse__(doc , self.__field_util__(fields[field]))
                
        elif callable(fields):
            return fields(doc) or ""
            
        else:
            return self.__parse__(doc , self.__field_util__(fields))

        return output

def main(args):
    output = dict({})
    p = Parser()    

    try:
        imp = importlib.import_module(args[0])
        form = imp.form
        if type(form) != dict:
            raise AttributeError("Declared form variable needs to be of type dictionary")
        
        for url in form:
            doc = fetch_doc(url)

            if type(doc) != str:
                output[url] = p.parse(doc, form[url])
            else:
                output[url] = doc

        save(args[1] , output)

    except AttributeError as e:
        print("[FATAL] {}.py doesn't seem to have a \"form\" attribute".format(args[0]))
    except ModuleNotFoundError as e:
        print("[FATAL] {}.py was found on /src".format(e.args[0]))
    except Exception as e:
        print("[FATAL] unknown error while initializing parser.")
        
def __parse_args__(args):
    form_name = "form"
    output_file = "dumps.json"

    l = len(args)

    if l >= 1 and args[0].startswith("-"):
        form_name = args[0][1:]

    if l >= 2 and args[1].startswith("-"):
        output_file = args[1][1:]

    if l >= 3:
        supported_formats = [".json" , ".csv"]
        try:
            supported_formats.index(args[2])
            output_file += args[2]
        except Exception:
            print("[WARN] Output format {} is not supported, defaulted to .json\n".format(args[2]))
            output_file += supported_formats[0]

    print("""Starting Parameters:
    Form Used   : {}.py
    Output File : {}
    """.format(form_name , output_file)
    )
    return [form_name  , output_file]

if __name__ == "__main__":
    print("Starting Sopp Script...\n")

    sys.argv.pop(0)

    main(__parse_args__(sys.argv))