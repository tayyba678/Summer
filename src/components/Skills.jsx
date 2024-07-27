import React from "react";
import p2 from "../assessts/p2.jpg"

const Skills= () =>{
    return(
        <div id="skills" className="w-full bg-[#1f1f22dc] py-16 px-4">
            <div className="max-w-[1200px] mx-auto grid md:grid-cols-2 ">
            <img className="mx-auto w-[400px] h-[400px] my-4" src={p2} alt="/" />
            <div className="flex flex-col justify-center p-4 m-4">
            <p className="md:text-4xl sm:text-3xl text-2xl font-bold py-2 text-[#e44fbf]">Professional Skills</p>
            <h1 className="md:text-3xl sm:text-2xl text-xl py-2 font-medium text-[#ffffff]">Front-end Developer Back-end Developer</h1>
            <p className="md:text-medium sm:text:small text-xsfont-small text-[#ffffff]">Proficient in C, C++, C#, Python, SQL, HTML, and CSS, adept at versatile application development, database management for efficient data handling, and front-end development creating responsive and visually appealing user interfaces.</p>
            </div>
            </div>
            </div>
    )
}
export default Skills;
