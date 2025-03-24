"use client";

import React, { useState, FormEvent, useEffect } from 'react';
import { useParams } from 'next/navigation';
import Image from 'next/image';
import { postRequest } from '@/utils/globals';
import jwt from 'jsonwebtoken';
import  DOMPurify from 'dompurify';
// import { useTitle } from '@/context/TitleContext';
interface SignUpStatus {
  success: boolean;
  display: string;
}

interface UserDetails {
  name: string;
  token: string;
}
const SignUpForm: React.FC =  () => {
  // State to represent sign up status
  // const {setTitle} = useTitle();
  const [signUpStatus, setSignUpStatus] = useState<SignUpStatus>({ success: false, display: "" });
  const [googleLoginUrl, setGoogleLoginUrl] = useState<string | undefined>(undefined);
  const [userDetails, setUserDetails] = useState<UserDetails>({ name: "", token: "" });
  const params = useParams();
  const adminToken = params.adminToken;

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    
    const formData = {"userToken":userDetails.token};
    const response = await postRequest(`/api/admin/${adminToken}/login`,formData)
    
    if (response && !response.error) {
      setSignUpStatus({ success: true, display: "Successfully Logged In" });
    } else {
      setSignUpStatus({ success: false, display: response?.error || "Sign Up Failed" });
    }
    const submitter = (e.nativeEvent as SubmitEvent).submitter 
    if (submitter && submitter.id === "google" && googleLoginUrl) {
      window.location.href = googleLoginUrl?(`${googleLoginUrl}&adminToken=${adminToken}`):"/login";
    }
  };

  useEffect(() => {
    if (!adminToken) {
      window.location.href = "/login";
      return
    }
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('googleLoginUrl')) {
      const googleLoginUrl = urlParams.get('googleLoginUrl');
      const expectedUrl = "https://accounts.google.com"
      if (!googleLoginUrl?.startsWith(expectedUrl)){
        return
      }
      setGoogleLoginUrl(googleLoginUrl);
    }
    if (urlParams.has('userToken')) {
      const userToken = urlParams.get('userToken');
      const details = jwt.decode(userToken!);
      if (details && userToken && typeof details !== 'string' && 'name' in details) {
        setUserDetails({
          name: DOMPurify.sanitize(details.name as string),
          token: userToken,
        });
      }
    }
  }, []);

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const {value} = e.target;
    setUserDetails({ ...userDetails, "token":   value });
  }
  return (
    <>
    
    <section className="w-full flex flex-col items-center gap-8 justify-center h-screen">
      <h1 className = "text-7xl text-tetriary drop-shadow-[0_0_4px_#D8C55A]">Crocodile Pay <Image src = "/images/croc1.png" alt = "croc" width="175" height="175" className = "absolute left-1/2 -translate-x-1/2 bottom-0 translate-y-10 -z-10"/> </h1>
      <h2 className= "text-4xl">Your Go to Service to pay for Crocoitems</h2>
      <form className="flex flex-col gap-4 justify-center items-center w-full" onSubmit={handleSubmit} >
        <input
          className="bg-white border-2 border-highlight rounded-lg w-5/12 text-2xl px-4 py-2"
          type="text"
          name="userToken"
          placeholder="userToken"
          value={userDetails.token}
          onChange = {onChange}
          required
        />
        <button
          id = "login"
          type="submit"
          className="relative bg-tetriary/50 rounded-full text-secondary font-bold w-fit px-10 py-2 text-2xl hover:brightness-90 transition-all duration-200"
          dangerouslySetInnerHTML={{ __html: userDetails.name?`Login as ${userDetails.name}`:"Login" }}
        >
        </button>
        {/* <button id = "google" >
          Google Login
        </button> */}
      </form>

      {signUpStatus.display && !signUpStatus.success && (
        <p className="text-red-500 font-bold">{signUpStatus.display}</p>
      )}
      {signUpStatus.success && (
        <p className="text-green-500 font-bold">{signUpStatus.display}</p>
      )}

      <a
        className="underline text-blue-500 hover:brightness-125 transition-all duration-200"
        href="/signup"
      >
        Signup Instead?
      </a>
      
    </section>
    </>
  );
};

export default SignUpForm;
