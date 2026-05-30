/**
 * Test if Pattern 2 triggers for a specific pair of lines.
 */
import("./repair-fragmentation.mjs").then(({ joinFragmentedProse, cleanupBlankLines, isContinuationLine, isStandaloneItem, hasContinuationMarker }) => {
  // Simulate what cleanupBlankLines produces for the section
  const simLines = [
    "The returned value doesn't include the time",
    "",
    "zone offset.",
    "",
    "datetime2(7)",
  ];
  
  console.log("Input to joinFragmentedProse:");
  simLines.forEach((l, i) => console.log(`  ${i}: ${JSON.stringify(l)}`));
  
  const result = joinFragmentedProse(simLines);
  
  console.log("\nOutput of joinFragmentedProse:");
  result.forEach((l, i) => console.log(`  ${i}: ${JSON.stringify(l)}`));
  
  console.log("\nHas 'time zone offset': " + result.some(l => l.includes("time zone offset")));
}).catch(e => console.error("Error:", e));
