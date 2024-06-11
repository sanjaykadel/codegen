import gen_utils
u = gen_utils
uc = u.CHARS
dprint = u.dprint

#kam pani garos, with this Model, code also runs
#template_path=f'bepyMaster/mainProject/templates/{uc.place_model}/{uc.place_model}.jsx'
#file_sample_template_content=open(template_path,"r").read()

#todo: read from existing query and mutation files with placeholder
# write to that file , so no extra steps need there 
file_sample_template_content=r"""
#######################################################
# copy these to these files #
# will add auto adding later #
#######################################################
#models.py
from .MMMMMMMMMM.MMMMMMMMMMModels import *

#schema.py
from .MMMMMMMMMM.MMMMMMMMMMSchema import *
class Query(graphene.ObjectType):
    Mmmmmmmmmms = graphene.List(MMMMMMMMMMType)
    def resolve_Mmmmmmmmmms(self, info, **kwargs):
        return MMMMMMMMMM.objects.all()

class Mutation(graphene.ObjectType):
    MMMMMMMMMM_Save = MMMMMMMMMM_SaveMutation.Field()


# links.html #
<a href="/?_P_PAGE_=MMMMMMMMMM/MMMMMMMMMM.html">MMMMMMMMMM</a><br>


# don't forget to makemigrations, migrate #
#######################################################
python manage.py makemigrations
python manage.py migrate
#######################################################
  (venv) C:\project\bePyCode\bepyMaster\mainProject>python manage.py makemigrations
  Migrations for 'mainApp':
    mainApp\migrations\0004_my_test_employer.py
      - Create model MY_TEST_EMPLOYER

  (venv) C:\project\bePyCode\bepyMaster\mainProject>python manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, mainApp, sessions
  Running migrations:
    Applying mainApp.0004_my_test_employer... OK
#######################################################
"""



def GetCode(**kwargs):
    model = kwargs.get('model')
    content=file_sample_template_content

    content = content.replace(uc.place_model, model.name)
    content = content.replace(uc.place_model_gql, model.name_gql)
    return content

def write_code(**kwargs):
    model=kwargs.get('model')
    # model_name = model.get('name')
    # out_dir = f'{uc.out_loc_prefix}bepyMaster/mainProject/mainApp/templates/{model_name}'
    # dprint(out_dir)

    # import os
    # os.makedirs(out_dir,exist_ok=True)

    str_model_content = GetCode(model=model)
    print(str_model_content)

    # out_file=f'{out_dir}/{model_name}.jsx'
    # f = open(out_file,'w')
    # f.write(str_model_content)
    # f.close()
    
    pass

if __name__ == '__main__':
    write_code(model=model)
    pass 


