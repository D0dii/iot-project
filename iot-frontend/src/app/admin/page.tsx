import { VotingForm } from "@/components/VotingForm";
import { columns } from "./columns";
import { DataTable } from "./data-table";

export interface Voting {
  id: number;
  name: string;
  votesFor: number;
  votesAgainst: number;
  votesWithheld: number;
}

export const votings: Voting[] = [
  {
    id: 1,
    name: "Głosowanie nr 82",
    votesFor: 280,
    votesAgainst: 100,
    votesWithheld: 72,
  },
  {
    id: 2,
    name: "Głosowanie nr 83",
    votesFor: 200,
    votesAgainst: 180,
    votesWithheld: 72,
  },
  {
    id: 3,
    name: "Głosowanie nr 84",
    votesFor: 200,
    votesAgainst: 180,
    votesWithheld: 72,
  },
  {
    id: 4,
    name: "Głosowanie nr 85",
    votesFor: 200,
    votesAgainst: 180,
    votesWithheld: 72,
  },
  {
    id: 5,
    name: "Głosowanie nr 86",
    votesFor: 200,
    votesAgainst: 180,
    votesWithheld: 72,
  },
];

export default function Home() {
  const data = votings;

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
