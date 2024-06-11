import ENV

def dprint(*kwargs):
    #print(kwargs)
    pass

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

# loops callback for each rows
def UtilsGetRowsCallback(**kwargs):
    fnCallback = kwargs.get('fnCallback')

    model = kwargs.get('model')

    model_name = model.get('name')
    model_columns = model.get('columns')
    
    dprint(model)
    dprint(model_name)
    dprint(model_columns)

    x=""
    for k in model_columns.keys():
        curr_col = model_columns[k]
        
        # cc = {} #current column to pass to callback
        # cc['name']=k
        # cc['type']=curr_col.get('type')
        # cc['length']=curr_col.get('length')
        # cc['fe_gql_type']=curr_col.get('fe_gql_type')
        curr_col['name']=k
        
        cc=curr_col
        
        
        x+=fnCallback(model=model, current_column=cc, current_column_obj=dotdict(cc))
    
    return x

"""
Generates columns, by passing fnCallback
from following structure

//s1s1s1s1s1
    var query_request = `
        query{
          MMMMMMMMMMs{
            id,
            bankId,
            name,
            address
          }
        }
    `;
//s1s1s1s1s1
"""
def GenPlaceholderSrc(**kwargs):
    model=kwargs.get('model')
    orgSrc=kwargs.get('orgSrc')
    placeholder=kwargs.get('placeholder') #todo: maybe pass placeholder1, placeholder2 if req
    fnCallback=kwargs.get('fnCallback')

    content2=""
    
    content1=orgSrc
    src = UtilsGetRowsCallback(model=model, fnCallback=fnCallback)
    dprint(src)
    pos1=content1.find(placeholder)
    pos2=content1.find(placeholder, pos1+1)
    content2=content1[:pos1]
    content2 += src
    content2 += content1[pos2+len(placeholder):]

    return content2

    # ref
    # src = u.UtilsGetRowsCallback(model=kwargs.get('model'), fnCallback=GetS1)
    # print(src)    
    # pos1=file_sample_template_content.find(uc.place_js1)
    # pos2=file_sample_template_content.find(uc.place_js1, pos1+1)
    # content=file_sample_template_content[:pos1]
    # content += src
    # content += file_sample_template_content[pos2:]

    # content1=content
    # src = u.UtilsGetRowsCallback(model=kwargs.get('model'), fnCallback=GetS2)
    # print(src)    
    # pos1=content1.find(uc.place_js2)
    # pos2=content1.find(uc.place_js2, pos1+1)
    # content2=content1[:pos1]
    # content2 += src
    # content2 += content1[pos2:]


#todo make dodict for chars eg:
chars={
    "tab":' ',
    "tab1":"    ", # space delimited tab
    "tab2":"        ","space":" ","nl":"\n",
    "BO":"{",
    "BC":"}",

    "place_model":"MMMMMMMMMM",
    "place_model_gql":"Mmmmmmmmmm",

    "place_s1":"#s1s1s1s1s1",
    "place_s2":"#s2s2s2s2s2",
    
    "place_js1":"										",
    "place_js2":"					     					", 
    "place_js3":"      						      ",

    "place_jc1":"//s1s1s1s1s1",
    "place_jc2":"//s2s2s2s2s2",

    "place_jsx1":"{/*s1s1s1s1s1*/}",

    "out_loc_prefix":"gen/" #todo: def input loc prefix (or a fn to get that, in_loc_prefix)
} # in json format
CHARS=dotdict(chars)

CHARS.out_loc_prefix = ENV.out_loc_prefix
CHARS.input_loc_prefix = ENV.input_loc_prefix



