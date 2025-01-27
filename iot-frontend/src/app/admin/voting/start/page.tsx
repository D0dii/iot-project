"use client";
import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { useRouter } from "next/navigation";

interface Question {
  id: number;
  title: string;
  question: string;
  is_active: boolean;
}

export default function Home() {
  const [currentQuestion, setCurrentQuestion] = useState<Question | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  async function fetchLatestQuestion() {
    try {
      setLoading(true);
      const response = await fetch("http://127.0.0.1:8000/api/v1/questions/");
      const data: Question[] = await response.json();
      const latestQuestion = data.reduce((max, question) =>
        question.id > max.id ? question : max
      );
      setCurrentQuestion(latestQuestion);
    } catch (err) {
      setError(err as string);
    } finally {
      setLoading(false);
    }
  }

  async function endVoting() {
    if (!currentQuestion) return;

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/v1/questions/${currentQuestion.id}/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ is_active: false }),
        }
      );

      if (response.ok) {
        router.push("finished");
      } else {
        console.error("Nie udało się zakończyć głosowania.");
      }
    } catch (err) {
      console.error(err);
    }
  }

  useEffect(() => {
    fetchLatestQuestion();
  }, []);

  if (loading) {
    return <div>Ładowanie...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!currentQuestion) {
    return <div>Brak dostępnych głosowań.</div>;
  }

  return (
    <div className="flex justify-center items-center flex-col gap-4">
      <div className="text-2xl">{currentQuestion.title}</div>
      <div className="text-xl">{currentQuestion.question}</div>
      <Button onClick={endVoting} type="button">
        Zakończ głosowanie
      </Button>
    </div>
  );
}
