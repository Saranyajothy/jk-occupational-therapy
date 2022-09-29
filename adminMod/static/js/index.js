let DB;

let form = document.querySelector('form');
let firstName = document.querySelector('#first-name');
let lastName = document.querySelector('#last-name');
let address = document.querySelector('#address');
let mobile_ext = document.querySelector('#mobile_ext');
let mobile = document.querySelector('#mobile');
let date = document.querySelector('#date');
let time = document.querySelector('#time');
let symptoms = document.querySelector('#symptoms');
let appointment  = document.querySelector('#appointment');
let services = document.querySelector('#services');

document.addEventListener('DOMContentLoaded', () => {
     // create the database
     let ScheduleDB = window.indexedDB.open('Appointment', 1);

     // if there's an error
     ScheduleDB.onerror = function() {
          console.log('error');
     }
     // if everything is fine, assign the result is to the (letDB) instance 
     ScheduleDB.onsuccess = function() {
          // console.log('Database Ready');

          
          DB = ScheduleDB.result;

          showAppointment();
     }

   
     ScheduleDB.onupgradeneeded = function(e) {
          
          let db = e.target.result;
          
          let objectStore = db.createObjectStore('appointment', { keyPath: 'key', autoIncrement: true } );

        
          objectStore.createIndex('firstname', 'firstname', { unique: false } );
          objectStore.createIndex('lastname', 'lastname', { unique: false } );
          objectStore.createIndex('mobile-ext', 'mobile', { unique: false } );
          objectStore.createIndex('date', 'date', { unique: false } );
          objectStore.createIndex('time', 'time', { unique: false } );
          objectStore.createIndex('symptoms', 'symptoms', { unique: false } );
          objectStore.createIndex('submit', 'submit', { unique: false } );
          //console.log('Database ready and fields created!');
     }

     form.addEventListener('submit', addAppointment);

     function addAppointment(e) {
          e.preventDefault();
          let newConsultation = {
               firstname : firstName.value,
               lastname : lastName.value,
               
             mobileext : mobileExt.value,
             mobile : mobile.value,
               date : date.value,
            time : time.value,
               symptoms : symptoms.value
              
          }
          
          let transaction = DB.transaction(['appointment'], 'readwrite');
          let objectStore = transaction.objectStore('appointment');

          let request = objectStore.add(newAppointment);
                    request.onsuccess = () => {
               form.reset();
          }
          transaction.oncomplete = () => {
               //console.log('New schedule added');

               showAppointment();
          }
          transaction.onerror = () => {
              //console.log();
          }

     }
     function showAppointment() {
       
          while(appointment.firstChild) {
               appointment.removeChild(appointment.firstChild);
          }
         
          let objectStore = DB.transaction('appointment').objectStore('appointment');

          objectStore.openCursor().onsuccess = function(e) {
               
               let cursor = e.target.result;
               if(cursor) {
                    let AppointmentHTML = document.createElement('li');
                    AppointmentHTML.setAttribute('data-consultation-id', cursor.value.key);
                    AppointmentHTML.classList.add('list-group-item');
                    
                 
                    AppointmentHTML.innerHTML = `  
                         <p class="font-weight-bold">Patient Name:  <span class="font-weight-normal">${cursor.value.patientname}<span></p>
                          <p class="font-weight-bold">Contact:  <span class="font-weight-normal">${cursor.value.contact}<span></p>
                         <p class="font-weight-bold">Date:  <span class="font-weight-normal">${cursor.value.date}<span></p>
                         <p class="font-weight-bold">Time:  <span class="font-weight-normal">${cursor.value.time}<span></p>
                         <p class="font-weight-bold">Symptoms:  <span class="font-weight-normal">${cursor.value.symptoms}<span></p>
                    `;

                    
                    const cancelBtn = document.createElement('button');
                    cancelBtn.classList.add('btn', 'btn-danger');
                    cancelBtn.innerHTML = 'Cancel';
                    cancelBtn.onclick = removeAppointment;
               
                 
                    AppointmentHTML.appendChild(cancelBtn);
                    appointment.appendChild(AppointmentHTML);

                    cursor.continue();
               } else {
                    if(!appointment.firstChild) {
                        services.textContent = 'Change your visiting hours';
                         let noSchedule = document.createElement('p');
                         noSchedule.classList.add('text-center');
                         noSchedule.textContent = 'No results Found';
                         appointment.appendChild(noSchedule);
                    } else {
                        services.textContent = 'Cancel Your appointment'
                    }
               }
          }
     }

          function removeAppointment(e) {
       
          let scheduleID = Number( e.target.parentElement.getAttribute('data-appointment-id') );
         
          let transaction = DB.transaction(['appointment'], 'readwrite');
          let objectStore = transaction.objectStore('appointment');
         
          objectStore.delete(scheduleID);

          transaction.oncomplete = () => {
             
               e.target.parentElement.parentElement.removeChild( e.target.parentElement );

               if(!appointment.firstChild) {
                   
                    services.textContent = 'Change your visiting hours';
                   
                   let noSchedule = document.createElement('p');
                  
                   noSchedule.classList.add('text-center');
                   
                   noSchedule.textContent = 'No results Found';
                
                   appointment.appendChild(noSchedule);
               } else {
                   services.textContent = 'Cancel your Consultation'
               }
          }
     }




// const form = document.getElementById('form');
// const firstname = document.getElementById('firstname');
// const lastname = document.getElementById('lastname');
// const address= document.getElementById('address');
// const email = document.getElementById('email');
// const mobile_ext = document.getElementById('mobile_ext');
// const mobile = document.getElementById('mobile');
// const symptoms  = document.getElementById('symptoms');
// const datetime  = document.getElementById('date/time');

// form.addEventListener('submit', e => {
// 	e.preventDefault();
	
// 	checkInputs();
// });

// // function checkInputs() {
// // 	// trim to remove the whitespaces
// // 	const firstnameValue = firstname.value.trim();
// //      const lastnameValue = lastname.value.trim();
// //      const Value = firstname.value.trim();
// //      const firstnameValue = firstname.value.trim();
// // 	const emailValue = email.value.trim();
	
	
// 	if(firstnameValue === '') {
// 		setErrorFor(firstName, 'Firstname cannot be blank');
// 	} else {
// 		setSuccessFor(firstName);
// 	}
	
//     if(lastnameValue === '') {
// 		setErrorFor(lastName, 'Lastname cannot be blank');
// 	} else {
// 		setSuccessFor(lastName);
// 	}
//     if(addressValue === '') {
// 		setErrorFor(address, 'Address cannot be blank');
// 	} else {
// 		setSuccessFor(address);
// 	}
// 	if(emailValue === '') {
// 		setErrorFor(email, 'Email cannot be blank');
// 	} else if (!isEmail(emailValue)) {
// 		setErrorFor(email, 'Not a valid email');
// 	} else {
// 		setSuccessFor(email);
// 	}
	
// 	if(mobileValue === '') {
// 		setErrorFor(mobile, 'Mobile cannot be blank');
// 	} else {
// 		setSuccessFor(mobile);
// 	}
	
// 	// if(password2Value === '') {
// 	// 	setErrorFor(, 'Password2 cannot be blank');
// 	// } else if(passwordValue !== password2Value) {
// 	// 	setErrorFor(password2, 'Passwords does not match');
// 	// } else{
// 	// 	setSuccessFor(password2);
// 	// }
// }

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}













