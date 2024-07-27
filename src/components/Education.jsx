import React from "react";

const Education = () => {
    return (
        <div id="education" className="w-full bg-[#000000dc] py-16">
            <div className="max-w-[1200px] mx-auto px-4">
                <p className="md:text-5xl sm:text-4xl text-3xl font-bold py-4 text-[#e44fbf] text-center">Education</p>
                
                <div className="grid md:grid-cols-2 gap-8">
                    {[
                        {
                            year: "2023-2027",
                            institution: "University of Engineering and Technology Lahore",
                            program: "Computer Science",
                            detail: "CGPA: 3.54"
                        },
                        {
                            year: "2021-2023",
                            institution: "Punjab Group of Colleges",
                            program: "ICS-Physics",
                            detail: "Grade: A+"
                        },
                        {
                            year: "2019-2021",
                            institution: "Moon Public Schools",
                            program: "Matric-(Bio Science)",
                            detail: "Grade: A+"
                        }
                    ].map(({ year, institution, program, detail }) => (
                        <div key={year} className="bg-[#1a1a1a] p-6 rounded-lg shadow-lg">
                            <div className="flex items-center mb-4">
                                <h1 className="md:text-4xl sm:text-2xl text-xl font-bold text-[#e44fbf]">{year}</h1>
                            </div>
                            <h3 className="md:text-xl sm:text-l text-sm font-semibold text-white">
                                {institution}
                                <br />
                                {program}
                                <br />
                                {detail}
                            </h3>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Education;
