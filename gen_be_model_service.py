import gen_utils
u = gen_utils
uc = u.CHARS
dprint = u.dprint

#kam pani garos, with this Model, code also runs
template_path=f'bepyMaster/mainProject/mainApp/{uc.place_model}/{uc.place_model}Service.py'
file_sample_template_content=open(template_path,"r").read()
dprint(file_sample_template_content)

def GetCode(**kwargs):
    model = kwargs.get('model')
    content = file_sample_template_content
    return content.replace(uc.place_model, model.name)

def write_code(**kwargs):
    model=kwargs.get('model')
    model_name = model.get('name')
    out_dir = f'{uc.out_loc_prefix}bepyMaster/mainProject/mainApp/{model_name}'
    dprint(out_dir)

    import os
    os.makedirs(out_dir,exist_ok=True)

    str_model_content = GetCode(model=model)
    dprint(str_model_content)

    out_file=f'{out_dir}/{model_name}Service.py'
    f = open(out_file,'w')
    f.write(str_model_content)
    f.close()
    
    pass


if __name__ == '__main__':
    write_code(model=model)
    pass 


