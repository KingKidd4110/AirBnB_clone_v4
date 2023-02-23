$(document).ready(function () {
  const checkAmen = {};
  $(document).on('change', "input[type='checkbox']", function () {
    if (this.checked) {
      checkAmen[$(this).data('id')] = $(this).data('name');
    } else {
      delete checkAmen[$(this).data('id')];
    }
    const amenList = [];
    for (const key in checkAmen) {
      amenList.push(checkAmen[key]);
    }
    $('.amenities h4').text(amenList.join(', '));
  });
});
$.get('http://0.0.0.0:5001/api/v1/status/', function (data) {
  if (data.status === 'OK') {
    $('#api_status').addClass('available');
  } else {
    $('#api_status').removeClass('available');
  }
});

function displayPlaces (data) {
  const placesSection = document.querySelector('.places');

  data.forEach(place => {
    const placeArticle = document.createElement('article');
    placeArticle.innerHTML = `
    <h2>${place.name}</h2>\
    <p>${place.description}</p>\
    <p>${place.price_by_night} per night</p>\
    <p>Max guests: ${place.max_guest}</p>\
    <p>Number of bedrooms: ${place.number_rooms}</p>\
    <p>Number of bathrooms: ${place.number_bathrooms}</p>\
    `;
    placesSection.appendChild(placeArticle);
  });
}

$.fetch('http://0.0.0.0:5001/api/v1/places_search/', {
  method: 'POST',
  headers: { ContentType: 'application/json' },
  body: JSON.stringify({})
}).then(response => response.json())
  .then(data => {
    displayPlaces(data);
  });

const button = document.querySelector('Button');
button.addEventListener('click', () => {
  const checkedAmenities = document.querySelectorAll('input[type=checkbox]:checked');
  const amenityIds = Array.from(checkedAmenities).map(amenity => amenity.dataset.id);

  $.fetch('http://0.0.0.0:5001/api/v1/places_search/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ amenities: amenityIds })
  }).then(response => response.json())
    .then(data => {
      displayPlaces(data);
    });
});
