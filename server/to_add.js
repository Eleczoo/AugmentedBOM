<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>


$.post( "http://10.177.243.170:5000/postmethod", {
    javascript_data: JSON.stringify(pcbdata)
});



function createCheckboxChangeHandler(checkbox, references, row) {
    return function () {
  
      if (checkbox == "Sourced")
      {
        if (row.cells[1].lastChild.checked)
        {
          refs = ["BOX", "ADD"];
        }
        else
        {
          refs = ["BOX", "DEL"]
        }
        references.forEach(element => {
          refs.push(element[0])
        });
        
        $.post( "http://127.0.0.1:5000/postdraw", {
        javascript_data: JSON.stringify(refs)
      });
      }
  
        refsSet = getStoredCheckboxRefs(checkbox);
        

clearHighlightedFootprints();
highlightedNet = net;
var arr = ["NET", "ADD", net];
$.post( "http://127.0.0.1:5000/postdraw", {
    javascript_data: JSON.stringify(arr)
});
        drawHighlights();



function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
        left: rect.left + window.scrollX,
        top: rect.top + window.scrollY
    };
}

function render_Iframe(layerdict)
{
        // From a random item, get the context
    var ctx = layerdict["bg"].getContext("2d");
        
        document.querySelectorAll('iframe').forEach(iframe => iframe.remove());

        var bk_el = document.getElementById("backcanvas");
        div_top = getOffset(bk_el).top;
        div_left = getOffset(bk_el).left;
        div_height = bk_el.clientHeight;
        div_width = bk_el.clientWidth;

        ifrm = document.createElement("IFRAME");
        ifrm.setAttribute("src","http://127.0.0.1:5000/live");
        //ifrm.setAttribute("onmouseout","closeFrame()")
        ifrm.style.display = "block";
        ifrm.style.width = div_width+"px";
        ifrm.style.height = div_height+"px";
        ifrm.style.position = "absolute";
        ifrm.style.top=div_top+"px";
        ifrm.style.left=div_left+"px";
        ifrm.style.zIndex= "101";

        document.body.appendChild(ifrm);
        return true;
}	

// HERE 2
function redrawCanvas(layerdict) {
    if(layerdict.layer != "B")
    {
        prepareLayer(layerdict);
        drawBackground(layerdict);
        drawHighlightsOnLayer(layerdict);
    }
    else
    {
        // Clear everything in the canvas and put an iframe ??
        render_Iframe(layerdict);

    }

}