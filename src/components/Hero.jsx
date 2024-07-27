import React from "react";
const Hero= () =>{
return(
    <div id="home"className="text-white">
        <div className="max-w-[800px] mt-[-96px] w-full h-screen mx-auto text-center flex flex-col justify-center">
        <p className="text-[#e44fbf] py-3 font-bold">Committed to Excellence in Software Development</p>
        <h1 className="md:text-5xl sm:text-4xl text-3xl font-bold md:py-6">Transforming Ideas into Reality</h1>
        <div >
            <p className="md:text-4xl sm:text-2xl text-xl font-bold text-[#d468b9] py-4">Mern-Stack Developer</p>
            <p className="md:text-3xl sm:text-2xl text-xl font-bold md:pl-4 pl-2">
            Specializing in Front-end, Back-end, and Database Solutions </p>
            
            </div>
            <p className="md:text-2xl text-xl font-bold text-[#e7add9]"> </p>
        <button className="bg-[#e44fbf] w-[200px] rounded-md font-medium my-6 mx-auto py-3 text-black ">Get Started</button>
   
        </div>
       </div>
) 
}
export default Hero