from .MMMMMMMMMMModels import *
def MMMMMMMMMMSaveService(**kwargs):
    print('MMMMMMMMMMSaveService', kwargs)
    data = kwargs.get('data')
    MMMMMMMMMMDb=None
    
    id = data.pop('id', 0)
    if id:
        id = int(id)

    markedToDelete_ = data.pop('markedToDelete_', 0)
    if id:
        MMMMMMMMMMDb = MMMMMMMMMM.objects.get(pk=id)
        if markedToDelete_:
            MMMMMMMMMMDb.delete()
            MMMMMMMMMMDb=None
        else:
            for key, value in data.items():
                setattr(MMMMMMMMMMDb, key, value)
            MMMMMMMMMMDb.save()
    else:
        MMMMMMMMMMDb = MMMMMMMMMM.objects.create(**data)
    return MMMMMMMMMMDb