import { Question } from "@/types/types";

//robie get'a na wszystkie pytania
//i biore to z najwiekszym id - czyli najnowsze
//jesli jest nieaktywne to zwracam nulla
export async function getLatestQuestion(): Promise<Question | null> {
  const response = await fetch("http://127.0.0.1:8000/api/v1/questions/");
  const questions = await response.json();
  if (questions.length === 0) return null;
  const latestQuestion = questions.reduce((max: Question, question: Question) =>
    question.id > max.id ? question : max
  );
  return latestQuestion.is_active ? latestQuestion : null;
}
