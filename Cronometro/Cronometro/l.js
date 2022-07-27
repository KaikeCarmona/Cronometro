var sec=60
var min=0
var hr=0
var pausa = false;
 
 
function twoDigits(digit){
    if(digit<10){
        return('0'+digit)
    }else{
        return(digit)
    }
}


function start(){

    if (pausa === false){
        min=24
    }
    watch()
    interval= setInterval(watch,1000)

 }

function pause(){
    clearInterval(interval)
    pausa=true; 
}

function reset(){
    clearInterval(interval)
    sec=59
    min=24
    window.alert("You've stopped at: "+document.getElementById('watch').innerText)
    document.getElementById('watch').innerText='25:00'

}

function watch(){
     sec--
     if(sec==00){
         min--
         sec=60
    }
    parar()

    document.getElementById('watch').innerText= twoDigits(min)+'m'+':'+twoDigits(sec)+'s'
}
 
 function parar(){
    console.log(min,sec)
     if (min == 0 & sec == 1){
         sec = 00
        clearInterval(interval)
        
     }

 }

