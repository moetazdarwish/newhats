function selectservice() {
    temsl = document.getElementById('temsl').value
    console.log(temsl)
    window.location.href = '/setting/' + temsl 
}

function add_(item,action) {

    window.location.href = '/detail/' + item + '/'+action+'/'
}

function daydetail(item){
    enday = document.getElementById('enday').value
    window.location.href='/daylst/'+item+'/'+enday+'/'
}

function prod_(item,action) {

    window.location.href = '/prodDetails/' + item + '/'+action+'/'
}
function mycopy() {
    var copyText = document.getElementById("myInput");
    copyText.select();
    copyText.setSelectionRange(0, 99999); 
    navigator.clipboard.writeText(copyText.value);
    cpy = document.getElementById('cpy')
    cpy.innerHTML = ''
    cpy.innerHTML = '<span style="color: #006a5d;">Done</span>'
  
  }
function ValidateFileUpload() {

    var fuData = document.getElementById('photo')
    var FileUploadPath = fuData.value;
    
    
    if (FileUploadPath == '') {
        alert("Please upload an image");
    
    } else {
        var Extension = FileUploadPath.substring(FileUploadPath.lastIndexOf('.') + 1).toLowerCase();
    
    
    
        if ( Extension == "png" ||  Extension == "jpeg" || Extension == "jpg") {
    
    
                if (fuData.files && fuData.files[0]) {
    
                    var size = fuData.files[0].size;
                    
                    if(size > 538000){
                        alert("Maximum file size exceeds" +size);
                        fuData.value=''
                        return;
                    }else{
                        stat=document.getElementById('stat')
                        stat.innerHTML=''
                        stat.innerHTML='Done'
                      
                    }
                }
        } 
    else {
            alert("Photo only allows file types of GIF, PNG, JPG, JPEG and BMP. ");
        }
    }}

