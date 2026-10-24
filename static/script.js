document.addEventListener("DOMContentLoaded", function(){

    const newTask = document.querySelector("#task");
    const sumbit = document.querySelector("#sumbit");


   

   
    sumbit.disabled = true
    // remove.disabled = true
    newTask.onkeyup  = () => {
        if (newTask.value.length > 0){
            sumbit.disabled = false
        }
        else{
            sumbit.disabled = true
        }
    }


    document.querySelector("form").onsubmit = () => {
        const task = newTask.value
        const li = document.createElement("li");
        let cb = document.createElement("input")
        let btn = document.createElement("button")
        cb.type = "checkbox"
        btn.textContent = "delete the task"
        btn.onclick = () => {
            li.remove()
        }

        li.innerHTML = task
        li.appendChild(cb)
        li.appendChild(btn)
        
       
        document.querySelector("#tasks").append(li)
       

        newTask.value = ""
        sumbit.disabled = true

        

        return false;


    }
    
})