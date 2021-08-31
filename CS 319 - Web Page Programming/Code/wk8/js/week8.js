function dragStart(ev) {
    ev.dataTransfer.effectAllowed='move';
    ev.dataTransfer.setData("Text", ev.target.getAttribute('id'));
    ev.dataTransfer.setDragImage(ev.target,0,0);
    
    return true;
 }
         
 function dragEnter(ev) {
    event.preventDefault();
    return true;
 }
 
 function dragOver(ev) {
    return false;
 }
 
 function dragDrop(ev) {
    var src = ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(src));
    ev.stopPropagation();
    return false;
 }

 function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}

function checkPuzzle() {
	var Image1 = document.getElementById('div1').getElementsByTagName('img')[0].src;
    var Image2 = document.getElementById('div2').getElementsByTagName('img')[0].src;
    var Image3 = document.getElementById('div3').getElementsByTagName('img')[0].src;
    var Image4 = document.getElementById('div4').getElementsByTagName('img')[0].src;
	
    if (Image1.includes("rsImage02.jpg") && Image2.includes("rsImage.jpg")
        && Image3.includes("rummage_sale_week2-1.png") && Image4.includes("jpegat20012quality.jpg"))
    {
        document.getElementById("result").innerHTML = "You Win!";
    }
    else
    {
        document.getElementById("result").innerHTML =  "Try Again!";
    }
}