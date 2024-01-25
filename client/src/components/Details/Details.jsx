import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './Details.css'
function Details() {
  const { id } = useParams();
  const [propertyDetails, setPropertyDetails] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5000/house/${id}`);
        
        console.log("Done then...")
        if (!response.ok) {
          console.error('Property not found');
          return;
        }

        const data = await response.json();
        console.log(data)
        setPropertyDetails(data);
      } catch (error) {
        console.error('Error fetching property details', error);
      }
    };

    fetchData();
  }, [id]); // Re-run the effect when the id changes

  if (propertyDetails === null) {
    return <div>Loading...</div>;
  }

  if (!propertyDetails) {
    return <div>Property not found</div>;
  }

  return (

<> 
  <div className="more-details-title">
    <h1>Details</h1>
  </div>  
<div className='more-details-container'>


  {propertyDetails.map((property) => (
          <div className="item-extra-details" key={property.id}>

            <div className="extra-details-image">
              <img src={property.url} alt={`House ${property.id}`} />
            </div>
            
            <div className="extra-details">
              <h4>House Type: {property.housetype}</h4>
            <h4>Location: {property.location}</h4>
            <h4>Price: {property.price}</h4>
            <h4>Description: {property.description}</h4> 
            </div>                
   </div>
          
        ))}


        <div id="reviews">
    <h3>Reviews</h3>
    <form>
    <textarea placeholder='Write a Review'></textarea>
    <button>Submit</button>
    </form>
  </div>


  </div>

  
</>



  );
}

export default Details;
