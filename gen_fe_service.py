import gen_utils
u = gen_utils
uc = u.CHARS
dprint = u.dprint

#kam pani garos, with this Model, code also runs
template_path=f'bepyMaster/mainProject/templates/{uc.place_model}/{uc.place_model}Service.js'
file_sample_template_content=open(template_path,"r").read()

def GetS1(**k):
    c = k.get('current_column_obj')
    s=""

    comma=","
    if c.LAST_COLUMN:
        comma=""

    field_name = c.fe_gql_name if c.fe_gql_name else c.name #bank_id changes to bankId
    s = f"{field_name}{comma}"
    
    s = f"{uc.tab1}{s}{uc.nl}"
    return s

def GetS2(**k):
    c = k.get('current_column_obj')
    dprint(c)
    s=""
    
    comma=","
    #if c.LAST_COLUMN:
    #    comma=""
    
    field_name = c.fe_gql_name if c.fe_gql_name else c.name #bank_id changes to bankId
    if c.type=='int':
        # ${!state.id ? '' : `id:${state.id},`} 
        s = f"${uc.BO}!state.{field_name} ? '' : `{field_name}:${uc.BO}state.{field_name}{uc.BC}{comma}`{uc.BC}"
    elif c.type=='char':     
        # ${!state.name ? '' : `name:"${state.name}",`}   
        s = f"""${uc.BO}!state.{field_name} ? '' : `{field_name}:"${uc.BO}state.{field_name}{uc.BC}"{comma}`{uc.BC}"""
    else:
        s = f"add extra to codegen"
    
    s = f"{uc.tab1}{s}{uc.nl}"

    if c.LAST_COLUMN: #adding delete on service
        s += """    ${!state.markedToDelete_ ? '' : `markedToDelete_:${state.markedToDelete_}`}""" #no last comma here

    dprint(s)
    return s


def GetCode(**kwargs):
    model = kwargs.get('model')
    content = file_sample_template_content

    content=u.GenPlaceholderSrc(
        model=model,
        orgSrc=content,
        placeholder = uc.place_js1,
        fnCallback = GetS1
    )

    content=u.GenPlaceholderSrc(
        model=model,
        orgSrc=content,
        placeholder = uc.place_js2,
        fnCallback = GetS2
    )

    content=u.GenPlaceholderSrc(
        model=model,
        orgSrc=content,
        placeholder = uc.place_js3,
        fnCallback = GetS1
    )
    
    content = content.replace(uc.place_model, model.name)    
    content = content.replace(uc.place_model_gql, model.name_gql)
    return content

def write_code(**kwargs):
    model=kwargs.get('model')
    model_name = model.get('name')
    out_dir = f'{uc.out_loc_prefix}bepyMaster/mainProject/mainApp/templates/{model_name}'
    dprint(out_dir)

    import os
    os.makedirs(out_dir,exist_ok=True)

    str_model_content = GetCode(model=model)
    dprint(str_model_content)

    out_file=f'{out_dir}/{model_name}Service.js'
    f = open(out_file,'w')
    f.write(str_model_content)
    f.close()
    
    pass

if __name__ == '__main__':
    write_code(model=model)
    pass 


