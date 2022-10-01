var url = "https://graph.facebook.com/v14.0/100824376140659/messages";

var xhr = new XMLHttpRequest();
xhr.open("POST", url);

xhr.setRequestHeader("Authorization", "Bearer EAAGlQoSu89kBAMMwfo56wrqJ0Njd8H2iKCn5ZA1b0wiASTGLhIiC78enVFRMjYy7Kp8gdhOZClhmMTtzZBcb8B6GtNOk005FTLcfv9pUyIrZCdovk0ZAUmEEKk19jeJe5rSIsAUxRCZA3QxXaMPCfdNAhWBlgcLcvUgQCwDQtFAZASsn27tYKln");
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onreadystatechange = function () {
   if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      console.log(xhr.status);
      console.log("yes yes yes");
    }
      console.log(xhr.responseText);
   }};

var data = `{
    "messaging_product": "whatsapp",
    "to": "2348165201384",
    "type": "template",
    "template": {
       "name": "sample_shipping_confirmation",
       "language": {
           "code": "en_US",
           "policy": "deterministic"
       },
       "components": [
         {
           "type": "body",
           "parameters": [
               {
                   "type": "text",
                   "text": "{{code}}"
               }
           ]
         }
       ]
    }
}`;

xhr.send(data);
