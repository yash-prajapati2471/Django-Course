console.log("Hello world");

let fetchBtn = document.getElementById('fetchBtn');

fetchBtn.addEventListener('click',buttonClickHandler)

function buttonClickHandler(){
    console.log('You have clicked the fetchbtn');

    const xhr = new XMLHttpRequest();

    xhr.open('GET','yash.txt',true);

    xhr.onprogress = function(){
        console.log('on progress');
    }

    xhr.onload = function(){
        if(this.status === 200){
            console.log(this.responseText)
        }
        else{
            console.log('some error occured');
        }
    }

    xhr.send();
}