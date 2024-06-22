import InputForm from "@/components/InputForm";
import { Meteors } from "@/components/ui/meteors";
import React from 'react';

export default function HomePage() {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="w-full max-w-md p-8 bg-white shadow-lg rounded-lg">
          <h1 className="text-2xl font-bold mb-6 text-center">Welcome to the Home Page</h1>
          
      <InputForm />
    
        </div>
        <Meteors/>
      </div>
    )
  }
