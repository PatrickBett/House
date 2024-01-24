import React from 'react'
import { useEffect, useState } from 'react'
import "./Properties.css"
import Details from "../Details/Details";


function Properties() {
const[properties, setProperties]=useState([])
const[handle, setHandle]= useState([])
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:5000/house");
      const data = await response.json();
      // console.log(data)
      // console.log("yes")
      setProperties(data);
    };
    fetchData();
  }, []);

  const handleClick =(propertyid)=>{
   setHandle((properties)=>{
    if (properties.includes(propertyid)){
      return properties.filter((id)=>id !==propertyid )
    } else{
    return [...properties,propertyid]}
   })
    
   
  };

  return (
    <>
      <h1>Properties</h1>
      <div className="properties--1">
        {properties.map((property) => (
          <div className="item" key={property.id}>           
              <img src={property.url} />
            <h4>House Type: {property.housetype}</h4>
            <h4>Location: {property.location}</h4>
            <h4>Price: {property.price}</h4>
            <h4>Description: {property.description}</h4>
            <button onClick={()=>handleClick(property.id)} className="seemore--btn">see more</button>
            {handle.includes(property.id)&&(<Details key={property.id} />)}
          </div>
        ))}
      </div>
    </>
  );
}

export default Properties
