import React from "react";
import p1 from "../assessts/p1.jpg"

const About= () =>{
    return(
        <div id="about" className="w-full bg-[#1f1f22dc] py-16 px-4">
            <div className="max-w-[1200px] mx-auto grid md:grid-cols-2 ">
            <img className="mx-auto w-[500px] my-4" src={p1} alt="/" />
            <div className="flex flex-col justify-center p-4 m-4">
            <p className="md:text-4xl sm:text-3xl text-2xl font-bold py-2 text-[#e44fbf]">About Me</p>
            <h1 className="md:text-3xl sm:text-2xl text-xl py-2 font-medium text-[#ffffff]">Front-end Developer Back-end Developer</h1>
            <p className="md:text-medium sm:text:small text-xsfont-small text-[#ffffff]">I am a computer science student with a keen interest
                 in programming, databases, problem-solving, and
                  front-end development. Quick to learn, I enjoy 
                  expanding my skills and applying them to real-world 
                  challenges. I am passionate about using technology
                   to create innovative solutions.</p>
            </div>
            </div>
            </div>
    )
}
export default About;
