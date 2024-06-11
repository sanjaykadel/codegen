
//todo:
//SimpleTest
// will do crud once 
// SimpleTestP1 will be in fn 
// SimpleTestP2 will be in fn 
// in another if dleete is not set, then not deleted 

MMMMMMMMMM_TEST_ARGS={
	_TRY_ : 0,
	_TRY_MAX_ : 15
}

function MMMMMMMMMMServiceQueryTest(args) {
    if(!fnGlobalServiceTestConfig(args)){ return; }

    var state = {};
    args.state = state;
    args.fnCallback = (cdata) => {
        console.log('MMMMMMMMMMServiceQueryTest fnCallback', JSON.stringify(cdata))
    }
    MMMMMMMMMMServiceQuery(args)
}
MMMMMMMMMMServiceQueryTest(MMMMMMMMMM_TEST_ARGS);


G_MMMMMMMMMM_Id = 0
G_MMMMMMMMMMServiceSaveTestState = {
	//s1s1s1s1s1
    name: "test1",
    address: "street1"
	//s1s1s1s1s1
};
function MMMMMMMMMMServiceSaveTestCreate(args) {
    if(!fnGlobalServiceTestConfig(args)){ return; }

    MMMMMMMMMMServiceSave({
        state: G_MMMMMMMMMMServiceSaveTestState, fnCallback: (cdata) => {
            console.log("MMMMMMMMMMServiceSaveTestCreate", JSON.stringify(cdata))
            G_MMMMMMMMMM_Id= cdata?._RESPONSE_?.data?.MmmmmmmmmmSave?.MmmmmmmmmmObj.id
            if( !G_MMMMMMMMMM_Id ){
                console.error('MMMMMMMMMMServiceSaveTestCreate', 'Test Error', 'no id found')
            }
        }
    });
}
MMMMMMMMMMServiceSaveTestCreate(MMMMMMMMMM_TEST_ARGS)

G_MMMMMMMMMMUpdated=false;
function MMMMMMMMMMServiceSaveTestUpdate(args) {
    if(!fnGlobalServiceTestConfig(args)){ return; }

    if(!G_MMMMMMMMMM_Id && args._TRY_++ < args._TRY_MAX_){
        setTimeout(()=>MMMMMMMMMMServiceSaveTestUpdate(args), 1000);
        return;
    }

    G_MMMMMMMMMMServiceSaveTestState.id = G_MMMMMMMMMM_Id
    MMMMMMMMMMServiceSave({
        state: G_MMMMMMMMMMServiceSaveTestState, fnCallback: (cdata) => {
            console.log("MMMMMMMMMMServiceSaveTestUpdate", JSON.stringify(cdata))
            G_MMMMMMMMMMUpdated=true;
        }
    });
}

MMMMMMMMMMServiceSaveTestUpdate(MMMMMMMMMM_TEST_ARGS)

G_MMMMMMMMMMDeleted=false;
function MMMMMMMMMMServiceSaveTestDelete(args) {
    if(!fnGlobalServiceTestConfig(args)){ return; }

    if(!G_MMMMMMMMMMUpdated && args._TRY_++ < args._TRY_MAX_ ){
        setTimeout(()=>MMMMMMMMMMServiceSaveTestDelete(args), 1000);
        return;
    }

    G_MMMMMMMMMMServiceSaveTestState.markedToDelete_ = 1;
    MMMMMMMMMMServiceSave({
        state: G_MMMMMMMMMMServiceSaveTestState, fnCallback: (cdata) => {
            console.log("MMMMMMMMMMServiceSaveTestDelete fnCallback", JSON.stringify(cdata));
            var objDel = cdata?._RESPONSE_?.data?.MmmmmmmmmmSave?.MmmmmmmmmmObj;
            if(objDel){
                fngDebuggers({'ERROR': ['MMMMMMMMMMServiceSaveTestDelete fnCallback: deleted obj should be null', objDel]});
            }
            G_MMMMMMMMMMDeleted = true;
        }
    });
}

MMMMMMMMMMServiceSaveTestDelete(MMMMMMMMMM_TEST_ARGS)


function MMMMMMMMMMServiceSaveTestId0(args) {
    if(!fnGlobalServiceTestConfig(args)){ return; }

    MMMMMMMMMMServiceSave({
        state: {
			//s2s2s2s2s2
            "id": "",
            "name":"n0",
            "address": "a0"
			//s2s2s2s2s2
        },
        fnCallback: (cdata) => {
            console.log("MMMMMMMMMMServiceSaveTestId0", JSON.stringify(cdata));
            
            //`{"errors":[{"message":"Syntax Error: Expected Name, found ':'.","locations":[{"line":7,"column":13}]}]}`
            var MmmmmmmmmmObj=cdata?._RESPONSE_?.data?.MmmmmmmmmmSave?.MmmmmmmmmmObj
            if(!MmmmmmmmmmObj){
                fngDebuggers({'ERROR': ['MMMMMMMMMMServiceSaveTestId0', 'Test Error', 'empty string id should create in db', MmmmmmmmmmObj]});
            }
            
            MmmmmmmmmmObj.markedToDelete_ = 1; //redelete this 
            MMMMMMMMMMServiceSave({
                state: MmmmmmmmmmObj, fnCallback: (cdata) => {
                    console.log("MMMMMMMMMMServiceSave fnCallback redelete", JSON.stringify(cdata));
                    
                }
            });
            
        }
    });
}

MMMMMMMMMMServiceSaveTestId0(MMMMMMMMMM_TEST_ARGS)

//again try to get/update data after delte


//todo: 
// tests like these for backend service too
//todo:
//get single item query