import { Button } from "@/components/ui/button";
import { Voting, ApiVoting } from "@/types/types";
import Link from "next/link";

async function getLatestVoting(): Promise<Voting | null> {
  const response = await fetch("http://127.0.0.1:8000/api/v1/user-answers/");
  const data = await response.json();

  if (data.length === 0) {
    return null;
  }

  const votings: Voting[] = data.map((voting: ApiVoting) => ({
    id: voting.id,
    title: voting.title,
    question: voting.question,
    votesFor: voting.za,
    votesAgainst: voting.przeciw,
    votesWithheld: voting["wstrzymal sie"],
  }));

  const latestQuestion = votings.reduce((max: Voting, question: Voting) =>
    question.id > max.id ? question : max
  );

  return latestQuestion;
}

export function ButtonAsLink() {
  return (
    <Button asChild>
      <Link href="/admin">Wróć do panelu</Link>
    </Button>
  );
}

export default async function Home() {
  const latestVoting = await getLatestVoting();
  if (!latestVoting) {
    return (
      <div className="flex justify-center items-center">
        Brak dostępnych głosowań.
      </div>
    );
  }
  return (
    <div className="flex justify-center items-center flex-col gap-4">
      <div className="text-2xl">{latestVoting.title}</div>
      <div className="text-xl">{latestVoting.question}</div>
      <div className="font-semibold">{`Za: ${latestVoting.votesFor}`}</div>
      <div className="font-semibold">{`Przeciw: ${latestVoting.votesAgainst}`}</div>
      <div className="font-semibold">{`Wstrzymało się: ${latestVoting.votesWithheld}`}</div>
      <ButtonAsLink />
    </div>
  );
}
