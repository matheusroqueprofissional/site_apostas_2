function showloading(){

    const div = document.createElement("div");
    div.classList.add("c-loader");

    document.body.appendChild(div)

    setTimeout(()=> hideLoading(),2000);
    document.getElementById("c-loader").style.display = "block"

}

function hideLoading(){
    document.getElementById("c-loader").style.display = "none"
    const loadings = document.getElementById("c-loader");
    if(loadings.length){
        loadings[0].remove();
        

    }
    
}