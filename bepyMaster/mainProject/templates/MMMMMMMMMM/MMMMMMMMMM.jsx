class MMMMMMMMMMForm extends React.Component {
    constructor(props) {
        super(props);
        this.handleHumanInputChange = this.props.handleHumanInputChange;
    }
    
    render() {
        var MMMMMMMMMM = this.props.MMMMMMMMMM;
        return (
            <div>
                { fnIsDebug() && 
                    <div>
                        ID: 
                        <input
                            type="text"
                            value={MMMMMMMMMM.id}
                            onChange={this.handleHumanInputChange}
                            name="id"
                        /> <br/>
                    </div>
                }     
          </div>
        );
      }
}

class MMMMMMMMMMComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        MMMMMMMMMM:{},
        MMMMMMMMMMs:[],
      };

      this.handleHumanInputChange = this.handleHumanInputChange.bind(this);
      this.handleApiCreateMMMMMMMMMM = this.handleApiCreateMMMMMMMMMM.bind(this);
      this.handleApiUpdateMMMMMMMMMM = this.handleApiUpdateMMMMMMMMMM.bind(this);
      this.handleApiDeleteMMMMMMMMMM = this.handleApiDeleteMMMMMMMMMM.bind(this);

      this.handleUiLoadMMMMMMMMMM = this.handleUiLoadMMMMMMMMMM.bind(this);
      this.handleUiDeleteMMMMMMMMMM=this.handleUiDeleteMMMMMMMMMM.bind(this);
    }

    componentDidMount() {
      console.log("componentDidMount", this.state);
      this.fnMMMMMMMMMMInitialSetState();
      this.fetchMMMMMMMMMMs();
    }

    fnMMMMMMMMMMInitialSetState(){
        this.setState({
            MMMMMMMMMM:{
                //s1s1s1s1s1
                id: '',
                name:'',
                address:'',
                bankId:''
                //s1s1s1s1s1
            }
        });
    }

    handleHumanInputChange(e) {
        var MMMMMMMMMM = this.state.MMMMMMMMMM;
        MMMMMMMMMM[e.target.name]=e.target.value;
        this.setState({
            MMMMMMMMMM: MMMMMMMMMM,
        });
    }


    fetchMMMMMMMMMMs(){
      console.log('fetchMMMMMMMMMMs',this.state);
      MMMMMMMMMMServiceQuery({
        state:this.state.MMMMMMMMMM,
        fnCallback:(datac) => {
          console.log('fetchMMMMMMMMMMs fnCallback',datac);
          this.setState({
            MMMMMMMMMMs: datac._RESPONSE_.data.Mmmmmmmmmms
          });
        }
      });
    }
    
    handleApiCreateMMMMMMMMMM(e) {
      e.preventDefault();
      console.log('handleApiCreateMMMMMMMMMM',this.state);
      MMMMMMMMMMServiceSave(
        {
          state:this.state.MMMMMMMMMM,
          fnCallback: (data) =>{
            console.log("handleApiCreateMMMMMMMMMM fnCallback", data);
            this.fnMMMMMMMMMMInitialSetState();
            this.fetchMMMMMMMMMMs();  
          }
        }
      )
    }

    handleApiUpdateMMMMMMMMMM(e) {
      e.preventDefault();
      console.log('handleApiUpdateMMMMMMMMMM',this.state);
      MMMMMMMMMMServiceSave({
          state:this.state.MMMMMMMMMM,
          fnCallback: (data) => {
            console.log("handleApiUpdateMMMMMMMMMM fnCallback", data);
            this.fnMMMMMMMMMMInitialSetState();
            this.fetchMMMMMMMMMMs();  
          }
        });
    }

    handleApiDeleteMMMMMMMMMM(e) {
      e.preventDefault();
      console.log('handleApiDeleteMMMMMMMMMM',this.state);
      MMMMMMMMMMServiceSave({
          state: {
            id : this.state.MMMMMMMMMM.id,
            markedToDelete_ : 1
          },
          fnCallback: (data) => {
            console.log("handleApiDeleteMMMMMMMMMM fnCallback", data);
            this.fetchMMMMMMMMMMs();  
          }
        });

    }

    handleUiLoadMMMMMMMMMM(obj){
        console.log("handleUiLoadMMMMMMMMMM",obj);
        this.setState({MMMMMMMMMM:obj});
    } 

    handleUiDeleteMMMMMMMMMM(obj) {
        console.log("handleUiDeleteMMMMMMMMMM", obj);
        MMMMMMMMMMServiceSave({
          state: {
            id : obj.id,
            markedToDelete_ : 1
          },
          fnCallback: (data) => {
            console.log("handleUiDeleteMMMMMMMMMM fnCallback", data);
            this.fetchMMMMMMMMMMs();
            this.fnMMMMMMMMMMInitialSetState();
          }
        });
    }


    render() {
      const { MMMMMMMMMM } = this.state;
      
      return (
        <div >
          <h1> Create, Update MMMMMMMMMM and Delete</h1>
          
          <form onSubmit={this.handleApiCreateMMMMMMMMMM}>
			{/*s1s1s1s1s1*/}
            { fnIsDebug() && <div>
                ID: 
                <input
                  type="text"
                  value={this.state.MMMMMMMMMM.id}
                  onChange={this.handleHumanInputChange}
                  name="id"
                /> <br/>
            </div>}

            Name: 
            <input
                type="text"
                value={MMMMMMMMMM.name}
                onChange={this.handleHumanInputChange}
                name="name"
            /> <br/>

            Address::
            <input
                type="text"
                value={ MMMMMMMMMM.address}
                onChange={this.handleHumanInputChange}
                name="address"
            /> <br/>

            Bank:
            <input
                type="text"
                value={ MMMMMMMMMM.bankId}
                onChange={this.handleHumanInputChange}
                name="bankId"
            /> <br/>
			{/*s1s1s1s1s1*/}

            {/* <MMMMMMMMMMForm 
                handleHumanInputChange={this.handleHumanInputChange} 
                MMMMMMMMMM={this.state.MMMMMMMMMM} /> */}

            <button type="submit">Create MMMMMMMMMM</button>
            <button type="submit"onClick={this.handleApiUpdateMMMMMMMMMM}>Update MMMMMMMMMM</button>
            <button type="button" onClick={this.handleApiDeleteMMMMMMMMMM}>Delete MMMMMMMMMM</button>
          </form>

          <ul style={_G_FIX_VH_STYLE_}>
            {this.state.MMMMMMMMMMs.map((obj) => (
              <li key={obj.id}>
                {obj.id}-{obj.name} - {obj.address}
                <button onClick={()=>this.handleUiLoadMMMMMMMMMM(obj)}>Edit</button>
                <button onClick={()=>this.handleUiDeleteMMMMMMMMMM(obj)}>Delete</button>
              </li>  
            ))}
          </ul>

        <StateDebugComponent display={this.state}/>         
        </div>
      );
    }
  }

  // Render your React component to the DOM
  ReactDOM.render(<MMMMMMMMMMComponent />, document.getElementById("root"));
