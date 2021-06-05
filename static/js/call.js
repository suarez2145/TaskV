
let csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
let app = new Vue({

    

    el: '#app',
    delimiters: ["[[","]]"],
    data: {

        newEmployee:{
            
            name:"",
            role:"",
            manager:"",
            worksite:"",
        },

        newWorksite:{
            name:"",
            address:"",
            owner:"",
            contact_info:"",
            codes_notes:"",
            item_set:""

        },
            //  need to make method below to create new checklist item and pass data to this data set and pass to page
        newChecklistitem:{
            item_text:"",
            is_complete: false,
            worksite:""

        },



        checklistMaker:{
            onscreen:false,
            worksite:{},
        },
        
        checkitems:{},
        EditEmployee: false,
        results:{},
        worksites:{},
        roles:["STD","MGR","SRMGR","PRES"]
    },

    methods: {

            //  need to make button to call this method to display checklists 
        gotoChecklist:function(worksite){
            this.checklistMaker.onscreen = true
            this.checklistMaker.worksite = worksite


        },

        getItems:function(){
            axios({
                
                method: 'get',
                baseURL: "../api/item/",
                params:{
                    
                    
                
            
                },
                


            })

            .then((response) => {this.checkitems = response.data
                console.log(response.data)
            })
        

            .catch(function(error){
                console.log(error)
            });

        },
        





        getEmployees:function(){
            axios({
                
                method: 'get',
                baseURL: "../api/employee/",
                params:{
                    
                    
                
            
                },
                


            })

            .then((response) => {this.results = response.data
                console.log(response.data)
            })
        

            .catch(function(error){
                console.log(error)
            });

        },



        
        addNewEmployee:function(){

            axios({
                
                method: 'post',
                baseURL: "../api/employee/",
                headers: {
                    "X-CSRFToken": csrf_token,
                    "Content-Type": "application/json"
                },
                data:{
                    name:this.newEmployee.name,
                    role:this.newEmployee.role,
                    manager:this.newEmployee.manager,
                    worksite_id:this.newEmployee.worksite

                }

            })
            .then(res => this.getEmployees())
            .then( res => console.log(res))
        },  



        DeleteWorksites:function(id,index){
            
            axios({
                
                method: 'delete',
                baseURL: "../api/worksite/"+ id,
                headers: {
                    "X-CSRFToken": csrf_token
                },

            })
                
            .then( res => this.worksites.splice(index,1))
            .then(res => this.getWorksites())
        },




        DeleteEmployees:function(id,index){
            
            axios({
                
                method: 'delete',
                baseURL: "../api/employee/"+ id,
                headers: {
                    "X-CSRFToken": csrf_token
                },

            },
                
            ).then( res => this.results.splice(index,1))},  




            UpdateEmployee:function(employee){
                axios({
                    
                    method: "put",
                    baseURL:`../api/employee/${employee.id}/`,
                    headers: {
                        "X-CSRFToken": csrf_token,
                        "Content-Type": "application/json",
                    },
                    data: employee 
    
    
    
                })
                .then(res => this.getEmployees())
                // closes the edit employee input window
                .then( res => this.EditEmployee = null);
            },


            
            getWorksites:function(){
                axios({
                    
                    method: 'get',
                    baseURL: "../api/worksite/",
                    params:{
                        
                        
                    
                
                    },
                    
    
    
                })
                
                .then((response) => {this.worksites = response.data
                    console.log(this.worksites)
                })
    
                .catch(function(error){
                    console.log(error)
                });
    
                
    
            },




            addNewWorksite:function(){
    
                axios({
                    
                    method: 'post',
                    baseURL: "../api/worksite/",
                    headers: {
                        "X-CSRFToken": csrf_token,
                        "Content-Type": "application/json"
                    },
                    data:{
                        name:this.newWorksite.name,
                        address:this.newWorksite.address,
                        owner:this.newWorksite.owner,
                        contact_info:this.newWorksite.contact_info,
                        codes_notes:this.newWorksite.codes_notes,
                        item_set:[],
    
    
                    }
    
                })
                .then(response => this.getEmployees())
                .then(response => this.getWorksites())
                .then(response =>{
                    console.log(response);
                    console.log(this.worksites)
                })
                // .then(res => this.getEmployees())
                // .then(res => this.getWorksites())
                // .then( res => console.log(res))
            }, 



        },

           
            
            
        mounted: function(){
         this.getEmployees();
         this.getItems();
         this.getWorksites();
             
        },
             
            
        


});

        

        




        






        

























    

    

    





