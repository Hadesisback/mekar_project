import InputForm from "@/components/InputForm";
import { FlipWords } from "@/components/ui/flip-words";
import { Meteors } from "@/components/ui/meteors";
import React from 'react';

const words = ["Name", "Identity Number", "Email", "Birth Date"];
export default function HomePage() {
    return (
      <div className=" bg-black flex justify-center items-center h-screen">
        <div className="w-full max-w-md p-8 bg-white shadow-lg rounded-lg">
          <h2 className="text-2xl mx-auto font-normal text-neutral-600 dark:text-neutral-400 text-center my-7">Input your<FlipWords words={words}/></h2>
          
      <InputForm />
    
        </div>
        <Meteors/>
      </div>
    )
  }
