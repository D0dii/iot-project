import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="flex justify-center items-center flex-col gap-4">
      <div className="text-2xl"> Głosowanie nr 82</div>
      <div className="text-xl">
        {" "}
        26. posiedzenie Sejmu Rzeczypospolitej Polskiej w dniach 8, 9 i 10
        stycznia 2025 r. - Wniosek o przerwę{" "}
      </div>
      <Button type="submit">Zakończ głosowanie</Button>
    </div>
  );
}
