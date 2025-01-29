export interface Voting {
  id: number;
  title: string;
  question: string;
  votesFor: number;
  votesAgainst: number;
  votesWithheld: number;
}

export interface ApiVoting {
  id: number;
  title: string;
  question: string;
  za: number;
  przeciw: number;
  "wstrzymal sie": number;
}

export interface Question {
  id: number;
  title: string;
  question: string;
  is_active: boolean;
}
