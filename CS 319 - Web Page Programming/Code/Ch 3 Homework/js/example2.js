function getPrices() {
  alert("Hello! I am an alert box!!");
  }

function runCode() {

  // PART ONE: CREATE HOTEL OBJECT AND WRITE OUT THE OFFER DETAILS
  // Create a hotel object using object literal syntax
  var hotel = {
    name: 'Grand',
    roomRate: 850, // Amount in dollars
    
    offerPrice: function() {
      var offerRate = this.roomRate * ((100 - arguments[0]) / 100);
      return offerRate;
    }
  };

  // Write out the hotel name, standard rate, and the special rate
  var hotelName, roomRate, specialRate1, specialRate2, specialRate3, numNights2, numNights35, numNights6;                    // Declare variables

  var discount2 = 15;   // Percentage discount <= 2 nights
  var discount35 = 20;  // Percentage discount > 3 <= 5 nights
  var discount6 = 30;   // Percentage discount > 5 nights
	
  hotelName = document.getElementById('hotelName');        // Get elements
  roomRate = document.getElementById('roomRate');
  specialRate1 = document.getElementById('specialRate1');
  specialRate2 = document.getElementById('specialRate2');
  specialRate3 = document.getElementById('specialRate3');
  numNights2 = document.getElementById('numNights2');
  numNights35 = document.getElementById('numNights35');
  numNights6 = document.getElementById('numNights6');

  hotelName.textContent = hotel.name;                      // Write hotel name
  roomRate.textContent =  '$' + hotel.roomRate.toFixed(2); // Write room rate
  specialRate1.textContent = '$' + hotel.offerPrice(discount2);       // Write offer price for <= 2 nights
  specialRate2.textContent = '$' + hotel.offerPrice(discount35);      // Write offer price for > 3 <= 5 nights
  specialRate3.textContent = '$' + hotel.offerPrice(discount6);       // Write offer price for > 5 nights
  numNights2.textContent = 'Rate for up to 2 nights';				  // Write number of nights for offer
  numNights35.textContent = 'Rate for 3 to 5 nights';				  // Write number of nights for offer
  numNights6.textContent = 'Rate for more than 5 nights';				  // Write number of nights for offer


  // PART TWO: CALCULATE AND WRITE OUT THE EXPIRY DETAILS FOR THE OFFER
  var expiryMsg; // Message displayed to users
  var today;     // Today's date
  var elEnds;    // The element that shows the message about the offer ending

  function offerExpires(today) {
    // Declare variables within the function for local scope
    var weekFromToday, day, date, month, year, dayNames, monthNames;

    // Add 3 days time (added in milliseconds)
    weekFromToday = new Date(today.getTime() + 3 * 24 * 60 * 60 * 1000);

    // Create arrays to hold the names of days / months
    dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    // Collect the parts of the date to show on the page
    day = dayNames[weekFromToday.getDay()];
    date = weekFromToday.getDate();
    month = monthNames[weekFromToday.getMonth()];
    year = weekFromToday.getFullYear();

    // Create the message
    expiryMsg = 'Offers expires next ';
    expiryMsg += day + ' <br />(' + date + ' ' + month + ' ' + year + ')';
    return expiryMsg;
  }

  today = new Date();                             // Put today's date in variable
  elEnds = document.getElementById('offerEnds');  // Get the offerEnds element
  elEnds.innerHTML = offerExpires(today);         // Add the expiry message
  btn = document.getElementById('specials');
  btn.textContent = "";

};