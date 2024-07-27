import React from "react";
const Contact= () =>{
return(
    <div id="contact" className="w-full py-16 bg-black text-white px-4">
        <div className="max-w-[1240px] mx-auto grid lg:grid-col-3">
            <div className="lg:col-span-2 my-4">
                <h1 className="md:text-4xl sm:text-3xl text-2xl text-[#e44fbf] font-bold py-2">Contact Me </h1>
                <p>Write your message in the box!</p>
            </div>
            <div className="my-4">
                <div className="flex flex:col sm:flow-row justify-between items-center w-full">
                    <input className="p-3 flex w-full rounded-md text-black"
                    type='email'
                    placeholder="Enter Email"/>
                    
                    <input className="p-3 m-10 flex w-full rounded-md text-black"
                    type='text'
                    placeholder="Enter Message"/>
                    <button className="bg-[#e44fbf] text-black rounded-md font-medium w-[200px] ml-4 mx-6 px-6 py-3">Submit</button>
                </div>
            </div>
        </div>
    </div>
) 
}
export default Contact