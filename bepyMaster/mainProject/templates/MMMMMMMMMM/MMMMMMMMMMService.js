function MMMMMMMMMMServiceQuery(args) {
    var state = args.state;

	//p1 nearby
    var query_request = `
        query{
          Mmmmmmmmmms{
										
            id,
            bankId,
            name,
            address
										
          }
        }
    `;
	//p1 nearby
	
    fetch(_G_GRAPHQL_URL_, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query_request })
    })
    .then((response) => response.json())
    .then((data) => {
        fnCallbackArgsResponse(args, data, query_request, 'MMMMMMMMMMServiceQuery')
    })
    .catch((error)=>{
        fnCallbackArgsResponse(args, error, query_request, 'MMMMMMMMMMServiceQuery')
    })
}
	

function MMMMMMMMMMServiceSave(args) {
    var state = args.state;
	
	//p2 here
    var data = `{					     					
        ${!state.id ? '' : `id:${state.id},`}
        ${!state.name ? '' : `name:"${state.name}",`}
        ${!state.address ? '' : `address:"${state.address}",`}
        ${!state.bankId ? '' : `bankId:${state.bankId},`}
        ${!state.markedToDelete_ ? '' : `markedToDelete_:${state.markedToDelete_},`}					     					}`;
	//p2 here


	//p3
    var query_request = `
    mutation{
        MmmmmmmmmmSave(

            data:${data}

        ){
            MmmmmmmmmmObj{      						      
                  id,
                  name,
                  address      						      
            }
        }
    }
    `;
	//p3


    fetch(_G_GRAPHQL_URL_, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query_request })
    })
    .then((response) => response.json())
    .then((data) => {
        fnCallbackArgsResponse(args, data, query_request, 'MMMMMMMMMMServiceSave')
    }).catch((error)=>{
        fnCallbackArgsResponse(args, error, query_request, 'MMMMMMMMMMServiceSave')
    })
}
