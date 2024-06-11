usage="""
usage: scr path_to_json_file
eg:
on windows
(venv) C:\projects\codegen>gen jsons/DCTB_SUBMISSION.json
(venv) C:\projects\codegen>gen ./jsons/MY_TEST_EMPLOYER.json

"""

#cls && rm -f ./gen/ && python gen.py
def dprint(*kwargs):
    print(kwargs)
    pass

import gen_utils
u = gen_utils


# read model from input json, or json in this dir
# that json converts into dict
#
# code will generate based on json files from the dir
#
# and ??????


if __name__ == '__main__':
    #from DCTB_SUBMISSION import model
    #json_file_path='DCTB_SUBMISSION.json'

    import os 
    import sys 
    CommandLine=sys.argv
    CL=CommandLine
    l = len(CL)

    if l > 1:
        json_file_path=CL[1]
    else:
        print(usage)
        sys.exit(1)

    import json;
    model=json.loads( open(json_file_path,"r").read() )
    model=u.dotdict(model)

    dprint(model)

    import gen_be_extras
    gen_be_extras.write_code(model=model)

    import gen_be_model
    gen_be_model.write_code(model=model)

    import gen_be_model_schema
    gen_be_model_schema.write_code(model=model)

    import gen_be_model_service
    gen_be_model_service.write_code(model=model)

    import gen_fe_html
    gen_fe_html.write_code(model=model)

    import gen_fe_jsx
    gen_fe_jsx.write_code(model=model)

    import gen_fe_service
    gen_fe_service.write_code(model=model)

    import gen_fe_test
    gen_fe_test.write_code(model=model)

    pass 




#todo:
# write tests such that
# we compare MMMMM and MMMMMMMM, both should be same identical, when generated
#
# and MMMMM orginal should work also
#
#
# later think about ?????, adding design, adding validation etc


# ideas ######
# generate required, not required validation from json
# or there is fnValidate for each field, write maybe custom js there if required
#
# similar could be done for backend

#
# write simple tests with no timeout
# conf for debug written to localstorage

# for testing
# js loaded in sequence
# bank loaded 1st,
# then employer js loaded