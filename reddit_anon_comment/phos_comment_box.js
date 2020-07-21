// Add Phos comment box to DOM
S=[]
S.push(document.createElement('form'))
S.push(document.createElement('textarea'))
S.push(document.createElement('div'))
S.push(document.createElement('button'))
S.push(document.createTextNode('PHOS'))
var style = document.createElement('style');
style.innerHTML = 'body {font-family: Arial, Helvetica, sans-serif;} * {box-sizing: border-box;} /* The popup chat - hidden by default */ .chat-popup {  display: none;  position: fixed;  bottom: 0;  right: 15px;  border: 3px solid #f1f1f1;  z-index: 9;} .open-button {  background-color: #555;  color: white;  padding: 16px 20px;  border: none;  cursor: pointer;  opacity: 0.8;  position: fixed;  bottom: 23px;  right: 28px;  width: 280px;}  .form-container {  max-width: 300px;  padding: 10px;  background-color: white; } .form-container textarea {  width: 100%;  padding: 15px;  margin: 5px 0 22px 0;  border: none;  background: #f1f1f1;  resize: none;  min-height: 200px; }　.form-container .btn {  background-color: #4CAF50;  color: white;  padding: 16px 20px;  border: none;  cursor: pointer;  width: 100%;  margin-bottom:10px;  opacity: 0.8;　}'
// Get the first script tag
var ref = document.querySelector('body');
// Insert our new styles before the first script tag
ref.parentNode.insertBefore(style, ref);
ref.append(S[2])
S[2].append(S[0])
S[0].append(S[3])
S[3].append(S[4])
S[2].className='chat-popup'
"chat-popup"
S[2].style.display='block'
S[0].append(S[1])
S[0].className='form-container'
S[1].className='form-container textarea'
"form-container textarea"
S[3].className='form-container btn'
S[3].style.backgroundColor='red'
S[3].onclick=function(){alert();}
S[0].style.backgroundColor='grey'
window.onbeforeunload = function(){ return 'Reload?';} // prevent page reload

