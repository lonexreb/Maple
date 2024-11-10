"use client";
import { expressionColors, isExpressionColor } from "./ExpressionColors";
import { motion } from "framer-motion";
import * as R from "remeda";

export default function Expressions({
  top3,
}) {

  return (
    <div
      className={
        "text-md w-full border-t border-border mt-2"
      }
    >
      {top3.map((exp) => (
        <div className={"w-full overflow-hidden mt-4"} key={exp[0]}>
          <div className={"flex items-center justify-between gap-1 font-mono pb-1"}>
            <div className={"font-medium truncate"}>{exp[0]}</div>
            <div className={"tabular-nums opacity-50"}>{(exp[1] * 100).toFixed(0)}%</div>
          </div>
          <div
            className={"relative h-2"}
            style={
              {
                "--bg": isExpressionColor(exp[0])
                  ? expressionColors[exp[0]]
                  : "var(--bg)",
              }
            }
          >
            <div
              className={
                "absolute top-0 left-0 size-full rounded-full opacity-10 bg-[var(--bg)]"
              }
            />
            <motion.div
              className={
                "absolute top-0 right-0 h-full bg-[var(--bg)] rounded-full"
              }
              initial={{ width: 0 }}
              animate={{
                width: `${R.pipe(
                  exp[1],
                  R.clamp({ min: 0, max: 1 }),
                  (value) => `${value * 100}%`
                )}`,
              }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}