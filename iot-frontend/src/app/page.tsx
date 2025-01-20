export default function Home() {
  return (
    <>
      <div className="bg-zinc-300 h-12 flex items-center p-3 w-full ">
        Trwa głosowanie...
      </div>
      <div className="flex justify-center items-center flex-col gap-4">
        <div className="text-5xl font-semibold"> Głosowanie nr 82</div>
        <div className="text-2xl">
          {" "}
          26. posiedzenie Sejmu Rzeczypospolitej Polskiej w dniach 8, 9 i 10
          stycznia 2025 r. - Wniosek o przerwę{" "}
        </div>
      </div>
    </>
  );
}
