const form=document.getElementById("upload-form");
const fileInput=document.getElementById("log-file");
const fileName=document.getElementById("file-name");
const dashboard=document.getElementById("dashboard");
const errorBox=document.getElementById("error");

fileInput.addEventListener("change",()=>{fileName.textContent=fileInput.files[0]?.name||"No file selected";});

form.addEventListener("submit",async(event)=>{
event.preventDefault(); errorBox.classList.add("hidden");
try{
const response=await fetch("/api/analyze",{method:"POST",body:new FormData(form)});
const result=await response.json();
if(!response.ok) throw new Error(result.error||"Analysis failed.");
document.getElementById("events").textContent=result.summary.events;
document.getElementById("alerts").textContent=result.summary.alerts;
document.getElementById("high").textContent=result.summary.high;
document.getElementById("critical").textContent=result.summary.critical;
document.getElementById("filename").textContent=result.filename;
document.getElementById("alert-list").innerHTML=result.alerts.length?result.alerts.map(a=>"<div class='alert'><span class='severity "+a.severity.toLowerCase()+"'>"+a.severity+"</span><strong>"+a.type+"</strong><p>"+a.message+"</p></div>").join(""):"<div class='alert'><strong>No detections</strong><p>No current rule matched the supplied events.</p></div>";
document.getElementById("event-list").innerHTML=result.events.slice(-100).reverse().map(e=>"<tr><td>"+e.timestamp+"</td><td>"+e.level+"</td><td>"+(e.ip||"—")+"</td><td>"+e.message+"</td></tr>").join("");
dashboard.classList.remove("hidden");
}catch(error){errorBox.textContent=error.message;errorBox.classList.remove("hidden");}
});
