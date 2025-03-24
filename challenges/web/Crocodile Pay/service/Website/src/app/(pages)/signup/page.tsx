"use client";

import React, { useState, FormEvent, ChangeEvent } from 'react';
import { postRequest } from '@/utils/globals';
import Image from 'next/image';
interface SignUpStatus {
  success: boolean;
  display: boolean;
}

const SignUpForm: React.FC = () => {
  // State to represent sign up status
  const [signUpStatus, setSignUpStatus] = useState<SignUpStatus>({ success: false, display: false });
  const [name, setName] = useState<string>('');

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const response = await postRequest('/api/signup',formData)
    if (response && !response.error) {
      setSignUpStatus({ success: true, display: true });
    } else {
      setSignUpStatus({ success: false, display: true });
    }
  };
  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const inputValue = event.target.value;
    // Allow only alphanumeric characters (a-z, A-Z, 0-9)
    const alphanumericValue = inputValue.replace(/[^a-zA-Z0-9]/g, '');
    setName(alphanumericValue);
  };

  return (
    <section className="w-full flex flex-col items-center gap-8 justify-center h-screen">
      <h1 className = "text-7xl text-tetriary drop-shadow-[0_0_4px_#D8C55A]">Crocodile Pay <Image src = "/images/croc1.png" alt = "croc" width="175" height="175" className = "absolute left-1/2 -translate-x-1/2 bottom-0 translate-y-10 -z-10"/> </h1>
      <h2 className= "text-4xl">Your Go to Service to pay for Crocoitems</h2>

      <form className="flex flex-col gap-4 justify-center items-center w-full" onSubmit={handleSubmit}>
        <input
          className="bg-white border-2 border-highlight rounded-lg w-5/12 text-2xl px-4 py-2"
          type="text"
          name="username"
          placeholder="Username"
          value={name}
          onChange={handleChange}
          required
        />
        <input
          className="bg-white border-2 border-highlight rounded-lg w-5/12 text-2xl px-4 py-2"
          type="password"
          name="password"
          placeholder="Password"
          
          required
        />
        <button
          type="submit"
          className="relative bg-tetriary/50 rounded-full text-secondary font-bold w-fit px-10 py-2 text-2xl hover:brightness-90 transition-all duration-200"
        >
          SIGN UP!
        </button>
      </form>

      {signUpStatus.display && !signUpStatus.success && (
        <p className="text-red-500 font-bold">Username Already Exists</p>
      )}
      {signUpStatus.success && (
        <p className="text-green-500 font-bold">Sign Up Successful</p>
      )}

      <a
        className="underline text-blue-500 hover:brightness-125 transition-all duration-200"
        href="/login"
      >
        Login Instead?
      </a>
    </section>
  );
};

export default SignUpForm;
