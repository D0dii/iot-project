"use client";

import { ColumnDef } from "@tanstack/react-table";
import { Voting } from "./page";
import { ArrowUpDown } from "lucide-react";
import { Button } from "@/components/ui/button";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.

export const columns: ColumnDef<Voting>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => {
      return (
        <div className="flex justify-center">
          <Button
            variant="ghost"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
          >
            ID
            <ArrowUpDown className="ml-1 h-4 w-4" />
          </Button>
        </div>
      );
    },
    cell: ({ row }) => {
      const cellValue: string = row.getValue("id");

      return <div className="flex justify-center">{cellValue}</div>;
    },
  },
  {
    accessorKey: "title",
    header: () => <div className="flex justify-center">Nazwa</div>,
    cell: ({ row }) => {
      const cellValue: string = row.getValue("title");

      return <div className="flex justify-center">{cellValue}</div>;
    },
  },
  {
    accessorKey: "votesFor",
    header: () => <div className="flex justify-center">Za</div>,
    cell: ({ row }) => {
      const cellValue: string = row.getValue("votesFor");

      return <div className="flex justify-center">{cellValue}</div>;
    },
  },
  {
    accessorKey: "votesAgainst",
    header: () => <div className="flex justify-center">Przeciw</div>,
    cell: ({ row }) => {
      const cellValue: string = row.getValue("votesAgainst");

      return <div className="flex justify-center">{cellValue}</div>;
    },
  },
  {
    accessorKey: "votesWithheld",
    header: () => <div className="flex justify-center">Wstrzymało się</div>,
    cell: ({ row }) => {
      const cellValue: string = row.getValue("votesWithheld");

      return <div className="flex justify-center">{cellValue}</div>;
    },
  },
];
