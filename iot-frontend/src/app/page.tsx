"use client";

import { useState, useEffect } from "react";
import { Question } from "@/types/types";
import { getLatestQuestion } from "@/utils/fetchQuestion";

export default function Home() {
  const [question, setQuestion] = useState<Question | null>(null);

  //Tutaj logika, żeby nie trzeba było odświeżać strony jak odpalimy w drugim oknie
  //to jest ten panel co będzie wyświetlany "w sejmie na ekranie"
  useEffect(() => {
    const fetchQuestion = async () => {
      const latestQuestion = await getLatestQuestion();
      setQuestion(latestQuestion);
    };

    fetchQuestion();

    const interval = setInterval(fetchQuestion, 2000);

    return () => clearInterval(interval);
  }, []);

  if (question === null) {
    return (
      <>
        <div className="bg-zinc-300 h-12 flex items-center p-3 w-full"></div>
        <div className="flex justify-center items-center flex-col gap-4">
          <div className="text-5xl font-semibold">
            Brak dostępnych głosowań.
          </div>
        </div>
      </>
    );
  }

  return (
    <>
      <div className="bg-zinc-300 h-12 flex items-center p-3 w-full">
        Trwa głosowanie...
      </div>
      <div className="flex justify-center items-center flex-col gap-4">
        <div className="text-5xl font-semibold">{question.title}</div>
        <div className="text-2xl">{question.question}</div>
      </div>
    </>
  );
}
