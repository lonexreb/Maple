
import React, { useRef, useEffect } from "react";

export default function ScrollContainer({children}) {
    const outerRef = useRef(null);
    const innerRef = useRef(null);
  
     // start the container at the bottom
    useEffect(() => {
      const outerHeight = outerRef.current.clientHeight;
      const innerHeight = innerRef.current.clientHeight;
  
      outerRef.current.scrollTo({
        top: innerHeight - outerHeight,
        left: 0
      });
    }, []);
  
    // scroll smoothly on change of children
    useEffect(() => {
      const outerHeight = outerRef.current.clientHeight;
      const innerHeight = innerRef.current.clientHeight;
  
      outerRef.current.scrollTo({
        top: innerHeight - outerHeight + 32,
        left: 0,
        behavior: "smooth"
      });
    }, [children]);
    
    return (
      <div
        ref={outerRef}
        style={{
          position: "relative", 
          height: "100%", 
          overflowY: "auto",
          overflowX: "hidden"
         }}
      >
        <div
          ref={innerRef}
          style={{
            position: "relative"
          }}
        >
          {children}
        </div>
      </div>
    )
  };
