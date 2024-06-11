import gen_utils
u = gen_utils
uc = u.CHARS
dprint = u.dprint

#kam pani garos, with this Model, code also runs
template_path=f'bepyMaster/mainProject/mainApp/{uc.place_model}/{uc.place_model}Schema.py'
file_sample_template_content=open(template_path,"r").read()

def GetDbField(**k):
    c = k.get('current_column_obj')
    dprint(c)
    
    s=""
    if c.type=='int':
        s = f"{c.name} = graphene.Int()"
    elif c.type=='char':        
        s = f"{c.name} = graphene.String()"
    else:
        s = f"add extra to codegen"
    
    if c.pk:
        s = f"{c.name} = graphene.ID()"

    s = f"{uc.tab1}{s}{uc.nl}"
    if c.LAST_COLUMN: #adding delete on service
        s += f"{uc.tab1}markedToDelete_ = graphene.Int(){uc.nl}"
    return s
    

def GetCode(**kwargs):
    model_name = kwargs.get('model').get('name')

    content=file_sample_template_content
    content=u.GenPlaceholderSrc(
        model=kwargs.get('model'),
        orgSrc=content,
        placeholder = uc.place_s1,
        fnCallback = GetDbField
    )
    
    return content.replace(uc.place_model, model_name)

def write_code(**kwargs):
    model=kwargs.get('model')
    model_name = model.get('name')
    out_dir = f'{uc.out_loc_prefix}bepyMaster/mainProject/mainApp/{model_name}'
    dprint(out_dir)

    import os
    os.makedirs(out_dir,exist_ok=True)

    str_model_content = GetCode(model=model)
    dprint(str_model_content)

    out_file=f'{out_dir}/{model_name}Schema.py'
    dprint(out_file)
    f = open(out_file,'w')
    f.write(str_model_content)
    f.close()
    
    pass


if __name__ == '__main__':
    write_code(model=model)
    pass 


