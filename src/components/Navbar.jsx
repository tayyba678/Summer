import React, { useState } from "react";
import { AiOutlineClose, AiOutlineMenu } from 'react-icons/ai'

const Navbar = () => {
    const [nav, setNav] = useState(false)
    const handleNav = () => {
        setNav(!nav)
    }
    const handleScroll = (id) => {
        const section = document.getElementById(id);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
        }
        setNav(false);
    };
    return (
        <div className='flex justify-between text-white items-center h-24 max-w-[1240px] mx-auto px-4'>
            <h1 className='w-full text-3xl font-bold text-[#e44fbf]'> Portfolio</h1>
            <ul className="hidden md:flex">
                <li className="p-4 cursor-pointer" onClick={() => handleScroll('home')}>Home</li>
                <li className="p-4 cursor-pointer" onClick={() => handleScroll('about')}>About Me</li>
                <li className="p-4 cursor-pointer" onClick={() => handleScroll('education')}>Education</li>
                <li className="p-4 cursor-pointer" onClick={() => handleScroll('skills')}>Skills</li>
                <li className="p-4 cursor-pointer" onClick={() => handleScroll('contact')}>Contact</li>
            </ul>
            <div onClick={handleNav} className="block md:hidden">
                {nav ? <AiOutlineClose size={20} /> : <AiOutlineMenu size={20} />}
            </div>
            <div className={nav ? "fixed top-0 left-0 w-[60%] h-full border-r-[#e44fbf] bg-black ease-in-out duration-500 " : 'fixed left-[-100%]'} >
                <h1 className='w-full text-3xl font-bold text-[#e44fbf] m-4'> Portfolio</h1>
                <ul className="uppercase p-4">
                    <li className="p-4 border-b border-[#e44fbf] cursor-pointer" onClick={() => handleScroll('home')}>Home</li>
                    <li className="p-4 border-b border-[#e44fbf] cursor-pointer" onClick={() => handleScroll('about')}>About Me</li>
                    <li className="p-4 border-b border-[#e44fbf] cursor-pointer" onClick={() => handleScroll('education')}>Education</li>
                    <li className="p-4 border-b border-[#e44fbf] cursor-pointer" onClick={() => handleScroll('skills')}>Skills</li>
                    <li className="p-4 border-b border-[#e44fbf] cursor-pointer" onClick={() => handleScroll('contact')}>Contact</li>

                </ul>
            </div>
        </div>
    )
}
export default Navbar