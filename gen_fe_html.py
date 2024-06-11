import gen_utils
u = gen_utils
uc = u.CHARS
dprint = u.dprint

#kam pani garos, with this Model, code also runs
template_path=f'bepyMaster/mainProject/templates/{uc.place_model}/{uc.place_model}.html'
file_sample_template_content=open(template_path,"r").read()
tab='    '

def GetDbField(**k):
    c = k.get('current_column_obj')
    s=""
    if c.type=='int':
        s = f"{c.name} = graphene.Int()"
    elif c.type=='char':        
        s = f"{c.name} = graphene.String()"
    else:
        s = f"add extra to codegen"
    
    s = f"{uc.tab1}{s}{uc.nl}"
    return s
    

def GetCode(**kwargs):
    model_name = kwargs.get('model').get('name')
    content=file_sample_template_content
    #src = u.UtilsGetRowsCallback(model=kwargs.get('model'), fnCallback=GetDbField)
    #print(src)

    
    # pos1=file_sample_template_content.find(uc.place_s1)
    # pos2=file_sample_template_content.find(uc.place_s1, pos1+1)

    # content=file_sample_template_content[:pos1]
    # content += src
    # content += file_sample_template_content[pos2:]
    
    return content.replace(uc.place_model, model_name)

def write_code(**kwargs):
    model=kwargs.get('model')
    model_name = model.get('name')
    out_dir = f'{uc.out_loc_prefix}bepyMaster/mainProject/mainApp/templates/{model_name}'
    dprint(out_dir)

    import os
    os.makedirs(out_dir,exist_ok=True)

    str_model_content = GetCode(model=model)
    dprint(str_model_content)

    out_file=f'{out_dir}/{model_name}.html'
    f = open(out_file,'w')
    f.write(str_model_content)
    f.close()
    
    pass


if __name__ == '__main__':
    write_code(model=model)
    pass 


