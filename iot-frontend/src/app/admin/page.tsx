import { VotingForm } from "@/components/VotingForm";
import { columns } from "./columns";
import { DataTable } from "./data-table";
import { Voting, ApiVoting } from "@/types/types";

async function getData(): Promise<Voting[]> {
  const response = await fetch("http://127.0.0.1:8000/api/v1/user-answers/");
  const data = await response.json();
  const votings: Voting[] = data.map((voting: ApiVoting) => ({
    id: voting.id,
    title: voting.title,
    question: voting.question,
    votesFor: voting.za,
    votesAgainst: voting.przeciw,
    votesWithheld: voting["wstrzymal sie"],
  }));
  return votings;
}

export default async function Home() {
  const data = await getData();

  return (
    <>
      <div className="flex justify-center text-2xl m-2">
        Wyniki poprzednich głosowań
      </div>
      <div className="mx-auto py-10 w-3/4">
        <DataTable columns={columns} data={data} />
      </div>
      <div className="mx-auto py-10 w-1/4">
        <VotingForm></VotingForm>
      </div>
    </>
  );
}
