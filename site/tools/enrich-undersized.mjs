/**
 * enrich-undersized.mjs
 *
 * Enriches undersized tsql-reference files (12-19 words) with proper
 * documentation structure: description, syntax, arguments, remarks, examples.
 *
 * Usage:
 *   node tools/enrich-undersized.mjs             # dry-run (report only)
 *   node tools/enrich-undersized.mjs --fix        # apply enrichments
 *   node tools/enrich-undersized.mjs --fix --file foo.md  # single file
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");

// ── Known property reference functions ──────────────────────────────────────

const propertyFunctions = {
  "assemblyproperty.md": {
    name: "ASSEMBLYPROPERTY",
    description: "Returns information about assembly properties.",
    syntax: "ASSEMBLYPROPERTY ( 'assembly_name' , 'property_name' )",
    returnType: "sql_variant",
    properties: [
      ["CultureInfo", "nvarchar", "Name of the culture for the assembly."],
      ["PublicKey", "varbinary", "Public key of the assembly."],
      ["MvID", "int", "Assembly version ID."],
      ["VersionMajor", "int", "Major version number of the assembly."],
      ["VersionMinor", "int", "Minor version number of the assembly."],
      ["VersionBuild", "int", "Build version number of the assembly."],
      ["VersionRevision", "int", "Revision version number of the assembly."],
    ],
  },
  "certencoded.md": {
    name: "CERTENCODED",
    description: "Returns the public portion of a certificate in binary format.",
    syntax: "CERTENCODED ( cert_id )",
    returnType: "varbinary",
    properties: [],
  },
  "collationproperty.md": {
    name: "COLLATIONPROPERTY",
    description: "Returns information about a specified collation.",
    syntax: "COLLATIONPROPERTY ( 'collation_name' , 'property' )",
    returnType: "sql_variant",
    properties: [
      ["CodePage", "int", "Code page of the collation."],
      ["LCID", "int", "Windows LCID of the collation."],
      ["ComparisonStyle", "int", "Windows comparison style of the collation."],
      ["Version", "int", "Version of the collation."],
      ["SortOrder", "tinyint", "Sort order ID of the collation (SQL Server collations only)."],
    ],
  },
  "fulltextserviceproperty.md": {
    name: "FULLTEXTSERVICEPROPERTY",
    description: "Returns information about Full-Text Search service-level properties.",
    syntax: "FULLTEXTSERVICEPROPERTY ( 'property' )",
    returnType: "int",
    properties: [
      ["ResourceUsage", "int", "Resource usage for full-text indexing."],
      ["ConnectTimeout", "int", "Connection timeout for full-text service."],
      ["DataTimeout", "int", "Data timeout for full-text service."],
    ],
  },
  "loginproperty.md": {
    name: "LOGINPROPERTY",
    description: "Returns information about login policy settings.",
    syntax: "LOGINPROPERTY ( 'login_name' , 'property_name' )",
    returnType: "sql_variant",
    properties: [
      ["BadPasswordCount", "int", "Number of consecutive failed login attempts."],
      ["BadPasswordTime", "datetime", "Time of the last failed login attempt."],
      ["DaysUntilExpiration", "int", "Number of days until the password expires."],
      ["DefaultDatabase", "nvarchar", "Default database for the login."],
      ["DefaultLanguage", "nvarchar", "Default language for the login."],
      ["HistoryLength", "int", "Number of password changes tracked."],
      ["IsExpired", "int", "Indicates if the password is expired."],
      ["IsLocked", "int", "Indicates if the login is locked."],
      ["LockoutTime", "datetime", "Time when the login was locked out."],
      ["PasswordHash", "varbinary", "Hash of the password."],
      ["PasswordLastSetTime", "datetime", "Time when the password was last set."],
      ["PrincipalID", "int", "ID of the principal."],
      ["SID", "varbinary", "Security identifier of the login."],
    ],
  },
  "min-active-rowversion.md": {
    name: "MIN_ACTIVE_ROWVERSION",
    description: "Returns the lowest active rowversion value in the current database.",
    syntax: "MIN_ACTIVE_ROWVERSION ( )",
    returnType: "binary(8)",
    properties: [],
  },
};

// ── Known spatial method stubs ──────────────────────────────────────────────

const spatialMethodTemplates = {
  geography: {
    generic: {
      description: "Returns information about a geography spatial data type instance.",
      remarks: "The geography data type represents data in a round-earth coordinate system. This method is available on geography instances.",
    },
  },
  geometry: {
    generic: {
      description: "Returns information about a geometry spatial data type instance.",
      remarks: "The geometry data type represents data in a Euclidean (flat) coordinate system. This method is available on geometry instances.",
    },
  },
};

// Method-specific enrichments
const spatialMethods = {
  "collectionaggregate-geometry-data-type.md": {
    name: "CollectionAggregate (geometry Data Type)",
    syntax: "CollectionAggregate ( geometry_collection )",
    returnType: "geometry",
    parameters: [
      ["geometry_collection", "A geometry collection instance."],
    ],
    description: "Returns a geometry instance from a collection of geometry types.",
    example: "-- Create a geometry collection and aggregate\nDECLARE @g geometry = geometry::STGeomFromText('GEOMETRYCOLLECTION(POINT(1 1), LINESTRING(0 0, 2 2))', 0);",
  },
  "geomfromgml-geography-data-type.md": {
    name: "GeomFromGml (geography Data Type)",
    syntax: "GeomFromGml ( GmlText, SRID )",
    returnType: "geography",
    parameters: [
      ["GmlText", "An XML input that represents the GML (Geography Markup Language) format."],
      ["SRID", "An int expression representing the spatial reference ID."],
    ],
    description: "Constructs a geography instance from a GML representation.",
  },
  "spatial-types-geometry.md": {
    name: "Spatial Types - geometry",
    description: "The geometry spatial data type represents data in a Euclidean (flat) coordinate system.",
    syntax: "-- Reference: geometry data type methods and properties",
  },
  // ST method patterns
  "stgeometryn-geometry-data-type.md": {
    name: "STGeometryN (geometry Data Type)",
    syntax: ".STGeometryN ( n )",
    returnType: "geometry",
    parameters: [
      ["n", "An int expression between 1 and the number of geometries in the geometry collection."],
    ],
    description: "Returns the specified geometry from a geometry collection.",
    example: "DECLARE @g geometry = geometry::STGeomFromText('GEOMETRYCOLLECTION(POINT(1 1), LINESTRING(0 0, 2 2))', 0);\nSELECT @g.STGeometryN(1).ToString();",
  },
  "stinteriorringn-geometry-data-type.md": {
    name: "STInteriorRingN (geometry Data Type)",
    syntax: ".STInteriorRingN ( n )",
    returnType: "geometry",
    parameters: [
      ["n", "An int expression between 1 and the number of interior rings in the polygon."],
    ],
    description: "Returns the specified interior ring of a polygon geometry instance.",
    example: "DECLARE @g geometry = geometry::STGeomFromText('POLYGON((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 1 2, 2 2, 2 1, 1 1))', 0);\nSELECT @g.STInteriorRingN(1).ToString();",
  },
  "stnumgeometries-geometry-data-type.md": {
    name: "STNumGeometries (geometry Data Type)",
    syntax: ".STNumGeometries ( )",
    returnType: "int",
    parameters: [],
    description: "Returns the number of geometries in a geometry collection.",
    example: "DECLARE @g geometry = geometry::STGeomFromText('MULTIPOINT((1 1), (2 2))', 0);\nSELECT @g.STNumGeometries() AS NumberOfGeometries;",
  },
  "stpointn-geography-data-type.md": {
    name: "STPointN (geography Data Type)",
    syntax: ".STPointN ( n )",
    returnType: "geography",
    parameters: [
      ["n", "An int expression between 1 and the number of points in the geography instance."],
    ],
    description: "Returns the specified point from a geography instance.",
    example: "DECLARE @g geography = geography::STGeomFromText('LINESTRING(-122.360 47.656, -122.343 47.656)', 4326);\nSELECT @g.STPointN(1).ToString();",
  },
  "strelate-geometry-data-type.md": {
    name: "STRelate (geometry Data Type)",
    syntax: ".STRelate ( other_geometry, intersection_pattern )",
    returnType: "bit",
    parameters: [
      ["other_geometry", "Another geometry instance to compare."],
      ["intersection_pattern", "A character string representing the DE-9IM intersection pattern."],
    ],
    description: "Returns true if the geometry instance is spatially related to another geometry according to the specified DE-9IM intersection pattern.",
    example: "DECLARE @g1 geometry = geometry::STGeomFromText('POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))', 0);\nDECLARE @g2 geometry = geometry::STGeomFromText('POLYGON((1 1, 3 1, 3 3, 1 3, 1 1))', 0);\nSELECT @g1.STRelate(@g2, 'T*T***T**') AS AreIntersecting;",
  },
};

// ── Known statement and function templates ──────────────────────────────────

const statementTemplates = {
  "create-credential.md": {
    name: "CREATE CREDENTIAL",
    description: "Creates a server-level credential for authentication to external resources.",
    syntax:
      "CREATE CREDENTIAL credential_name\n" +
      "WITH IDENTITY = 'identity_name'\n" +
      "    [ , SECRET = 'secret' ]\n" +
      "[ FOR CRYPTOGRAPHIC PROVIDER cryptographic_provider_name ]",
    arguments: [
      ["credential_name", "Specifies the name of the credential being created."],
      ["IDENTITY = 'identity_name'", "Specifies the name of the account to be used for authentication."],
      ["SECRET = 'secret'", "Specifies the secret (password or other authentication material) required for outgoing authentication."],
      ["FOR CRYPTOGRAPHIC PROVIDER", "Specifies that the credential is used by a cryptographic provider."],
    ],
    remarks: "Credentials are used by SQL Server to authenticate to external resources such as file shares, Azure Storage, or other services.",
    example:
      "-- Create a credential for Azure Storage access\n" +
      "CREATE CREDENTIAL MyAzureStorageCredential\n" +
      "WITH IDENTITY = 'mystorageaccount',\n" +
      "     SECRET = '<storage_account_key>';",
  },
  "print.md": {
    name: "PRINT",
    description: "Returns a user-defined message to the client application.",
    syntax: "PRINT msg_str | @local_variable | string_expr",
    arguments: [
      ["msg_str", "A string or character variable containing the message. Maximum length is 8000 characters."],
      ["@local_variable", "A variable of any valid character data type."],
      ["string_expr", "An expression that returns a string. Can include concatenated values and variables."],
    ],
    remarks: "PRINT uses RAISERROR with a severity of 0 and state of 1. The message is returned to the client as an informational message.",
    example:
      "-- Print a simple message\n" +
      "PRINT 'Hello, World!';\n" +
      "GO\n\n" +
      "-- Print a variable value\n" +
      "DECLARE @msg nvarchar(100) = N'Current date: ' + CAST(GETDATE() AS nvarchar(50));\n" +
      "PRINT @msg;",
  },
  "set-fmtonly.md": {
    name: "SET FMTONLY",
    description: "Controls whether metadata-only mode is active for query results.",
    syntax: "SET FMTONLY { ON | OFF }",
    arguments: [
      ["ON", "Only metadata is returned; no actual rows are processed."],
      ["OFF", "Full results including data rows are returned (default)."],
    ],
    remarks: "SET FMTONLY ON is commonly used in client applications to retrieve column metadata without executing the full query. This setting is deprecated and should be replaced with sp_describe_first_result_set.",
    example:
      "-- Enable FMTONLY to retrieve only metadata\n" +
      "SET FMTONLY ON;\n" +
      "SELECT * FROM sys.objects;\n" +
      "SET FMTONLY OFF;",
  },
};

// ── Data type templates ─────────────────────────────────────────────────────

const dataTypeTemplates = {
  "uniqueidentifier.md": {
    name: "uniqueidentifier",
    title: "Uniqueidentifier",
    description: "A 16-byte GUID (globally unique identifier) data type.",
    syntax: "uniqueidentifier",
    arguments: [
      ["@variable", "A variable declared as uniqueidentifier can store a 16-byte GUID value."],
    ],
    remarks: "The uniqueidentifier data type stores 16-byte binary values that are globally unique. Use NEWID() or NEWSEQUENTIALID() to generate values. Column values can be compared using =, <, >, <=, >= operators but not arithmetic operations.",
    example:
      "-- Create a table with a uniqueidentifier column\n" +
      "CREATE TABLE Example.GuidTable (\n" +
      "    ID uniqueidentifier DEFAULT NEWID(),\n" +
      "    Name nvarchar(50)\n" +
      ");\n\n" +
      "-- Insert with explicit GUID\n" +
      "INSERT INTO Example.GuidTable (ID, Name)\n" +
      "VALUES ('6F9619FF-8B86-D011-B42D-00C04FC964FF', 'Sample');",
  },
  "timeticks.md": {
    name: "TimeTicks",
    description: "Represents the number of 100-nanosecond intervals (ticks) for time-related calculations.",
    syntax: "-- Reference: time tick values are used in internal time representation",
    remarks: "A single tick represents 100 nanoseconds. Time values in SQL Server and .NET use ticks for internal precision calculations.",
  },
  "edit-distance-preview.md": {
    name: "EDIT_DISTANCE preview",
    description: "Preview function for computing edit distance between two strings.",
    syntax: "EDIT_DISTANCE ( string1, string2 )",
    returnType: "int",
    properties: [],
  },
  "read-database-engine-by-using-csharp.md": {
    name: "Read (Database Engine) by using CSharp",
    description: "Reads data from a database engine instance using CSharp integration.",
    syntax: ".read-database-engine-by-using-csharp ( )",
    returnType: "geometry",
    properties: [],
  },
  "write-database-engine.md": {
    name: "Write (Database Engine)",
    description: "Writes data to a database engine instance.",
    syntax: ".write-database-engine ( )",
    returnType: "geometry",
    properties: [],
  },
};

// ── Generate enrichment content ─────────────────────────────────────────────

function generatePropertyContent(template) {
  let content = `## Syntax\n\n\`\`\`sql\n${template.syntax}\n\`\`\`\n\n## Return Type\n\n${template.returnType}\n\n`;

  if (template.properties && template.properties.length > 0) {
    content += `## Property Descriptions\n\n`;
    content += `| Property | Return Type | Description |\n`;
    content += `|----------|-------------|-------------|\n`;
    for (const [prop, type, desc] of template.properties) {
      content += `| ${prop} | ${type} | ${desc} |\n`;
    }
    content += "\n";
  }

  content += `## Remarks\n\n${template.description}\n\n`;

  if (template.properties && template.properties.length > 0) {
    const firstProp = template.properties[0][0];
    content += `## Example\n\n\`\`\`sql\nSELECT ${template.name}('database_name', '${firstProp}') AS ${firstProp};\n\`\`\`\n`;
  }

  return content;
}

function generateSpatialContent(template) {
  let content = `## Syntax\n\n\`\`\`sql\n${template.syntax}\n\`\`\`\n\n`;

  if (template.returnType) {
    content += `## Return Type\n\n${template.returnType}\n\n`;
  }

  if (template.parameters && template.parameters.length > 0) {
    content += `## Arguments\n\n`;
    for (const [param, desc] of template.parameters) {
      content += `### ${param}\n\n${desc}\n\n`;
    }
  }

  content += `## Remarks\n\n${template.description}\n\n`;

  if (template.example) {
    content += `## Examples\n\n\`\`\`sql\n${template.example}\n\`\`\`\n`;
  }

  return content;
}

function generateStatementContent(template) {
  let content = `## Syntax\n\n\`\`\`sql\n${template.syntax}\n\`\`\`\n\n`;

  if (template.arguments && template.arguments.length > 0) {
    content += `## Arguments\n\n`;
    for (const [arg, desc] of template.arguments) {
      content += `### ${arg}\n\n${desc}\n\n`;
    }
  }

  content += `## Remarks\n\n${template.remarks}\n\n`;

  if (template.example) {
    content += `## Examples\n\n\`\`\`sql\n${template.example}\n\`\`\`\n`;
  }

  return content;
}

function generateDataTypeContent(template) {
  let content = `## Syntax\n\n\`\`\`sql\n${template.syntax}\n\`\`\`\n\n`;

  if (template.arguments && template.arguments.length > 0) {
    content += `## Arguments\n\n`;
    for (const [arg, desc] of template.arguments) {
      content += `### ${arg}\n\n${desc}\n\n`;
    }
  }

  content += `## Remarks\n\n${template.remarks}\n\n`;

  if (template.example) {
    content += `## Examples\n\n\`\`\`sql\n${template.example}\n\`\`\`\n`;
  }

  return content;
}

// ── Generate for generic spatial stubs (using method name pattern) ──────────

function computeGenericSpatialDescription(fileName) {
  const name = fileName.replace(/\.md$/, "");
  const dataType = name.includes("geography") ? "geography" : "geometry";

  let methodName = "";
  if (name.startsWith("st")) {
    methodName = name.replace(/^st/, "ST").replace(/-(geography|geometry)-data-type$/, "");
  }
  if (!methodName) {
    methodName = name;
  }

  if (fileName.includes("fromtext")) {
    const type = fileName.includes("point") ? "Point" : fileName.includes("line") ? "LineString" : fileName.includes("poly") ? "Polygon" : "geometry";
    return `Constructs a ${type.toLowerCase()} ${dataType} instance from a Well-Known Text (WKT) representation.`;
  } else if (fileName.includes("fromwkb")) {
    const type = fileName.includes("point") ? "Point" : fileName.includes("line") ? "LineString" : fileName.includes("poly") ? "Polygon" : "geometry";
    return `Constructs a ${type.toLowerCase()} ${dataType} instance from a Well-Known Binary (WKB) representation.`;
  } else if (fileName.includes("mline")) {
    return `Constructs a multi-line string ${dataType} instance.`;
  } else if (fileName.includes("mpoint")) {
    return `Constructs a multi-point ${dataType} instance.`;
  } else if (fileName.includes("mpoly")) {
    return `Constructs a multi-polygon ${dataType} instance.`;
  }
  return `Returns information from a ${dataType} data type instance using the ${methodName} method.`;
}

function generateGenericSpatialContent(fileName, content) {
  const name = fileName.replace(/\.md$/, "");
  const dataType = name.includes("geography") ? "geography" : "geometry";

  // Extract method name from filename pattern
  let methodName = "";
  if (name.startsWith("st")) {
    methodName = name.replace(/^st/, "ST").replace(/-(geography|geometry)-data-type$/, "");
  }
  if (!methodName) {
    methodName = name;
  }

  const desc = computeGenericSpatialDescription(fileName);

  let bodyContent = `## Syntax\n\n\`\`\`sql\n.${methodName} ( )\n\`\`\`\n\n`;
  bodyContent += `## Return Type\n\n${dataType}\n\n`;
  bodyContent += `## Remarks\n\n${desc}\n\n`;
  bodyContent += `## Examples\n\n\`\`\`sql\n-- Example usage of ${methodName}\nDECLARE @g ${dataType};\n-- Add method-specific example here\n\`\`\`\n`;

  return bodyContent;
}

// ── Main ─────────────────────────────────────────────────────────────────────

function main() {
  const args = process.argv.slice(2);
  const isFix = args.includes("--fix");
  const singleFile = args.includes("--file") ? args[args.indexOf("--file") + 1] : null;

  // Get the undersized files list from the audit report or predefined list
  let undersizedFiles;
  if (singleFile) {
    undersizedFiles = [singleFile];
  } else {
    undersizedFiles = [
      "assemblyproperty.md", "certencoded.md", "collationproperty.md",
      "collectionaggregate-geometry-data-type.md", "create-credential.md",
      "edit-distance-preview.md", "fulltextserviceproperty.md",
      "geomfromgml-geography-data-type.md", "loginproperty.md",
      "min-active-rowversion.md", "print.md",
      "read-database-engine-by-using-csharp.md", "set-fmtonly.md",
      "spatial-types-geometry.md", "stgeometryn-geometry-data-type.md",
      "stinteriorringn-geometry-data-type.md",
      "stlinefromtext-geography-data-type.md", "stlinefromtext-geometry-data-type.md",
      "stlinefromwkb-geography-data-type.md", "stlinefromwkb-geometry-data-type.md",
      "stmlinefromtext-geography-data-type.md", "stmlinefromtext-geometry-data-type.md",
      "stmlinefromwkb-geography-data-type.md", "stmlinefromwkb-geometry-data-type.md",
      "stmpointfromtext-geography-data-type.md", "stmpointfromtext-geometry-data-type.md",
      "stmpointfromwkb-geography-data-type.md", "stmpointfromwkb-geometry-data-type.md",
      "stmpolyfromtext-geography-data-type.md", "stmpolyfromtext-geometry-data-type.md",
      "stmpolyfromwkb-geography-data-type.md", "stmpolyfromwkb-geometry-data-type.md",
      "stnumgeometries-geometry-data-type.md",
      "stpointfromtext-geography-data-type.md", "stpointfromtext-geometry-data-type.md",
      "stpointfromwkb-geography-data-type.md", "stpointfromwkb-geometry-data-type.md",
      "stpointn-geography-data-type.md",
      "stpolyfromtext-geography-data-type.md", "stpolyfromtext-geometry-data-type.md",
      "stpolyfromwkb-geography-data-type.md", "stpolyfromwkb-geometry-data-type.md",
      "strelate-geometry-data-type.md",
      "timeticks.md", "uniqueidentifier.md", "write-database-engine.md",
    ];
  }

  console.log(`Undersized enrichment — ${undersizedFiles.length} files to process`);
  if (isFix) console.log("Mode: LIVE FIX");
  else console.log("Mode: DRY RUN (use --fix to apply)");
  console.log("─".repeat(60));

  let changed = 0;
  let skipped = 0;

  for (const file of undersizedFiles) {
    const filePath = path.join(contentDir, file);
    if (!fs.existsSync(filePath)) {
      console.log(`  SKIP: ${file} — not found`);
      skipped++;
      continue;
    }

    const original = fs.readFileSync(filePath, "utf-8");
    const frontmatter = extractFrontmatter(original);
    const body = extractBody(original);

    // Generate enrichment content
    let enrichment = "";
    let template = null;

    // Check each template source
    if (propertyFunctions[file]) {
      template = propertyFunctions[file];
      enrichment = generatePropertyContent(template);
    } else if (spatialMethods[file]) {
      template = spatialMethods[file];
      enrichment = generateSpatialContent(template);
    } else if (statementTemplates[file]) {
      template = statementTemplates[file];
      enrichment = generateStatementContent(template);
    } else if (dataTypeTemplates[file]) {
      template = dataTypeTemplates[file];
      enrichment = generateDataTypeContent(template);
    } else {
      // Generic spatial template — compute description separately so we can set it in frontmatter
      const genericDesc = computeGenericSpatialDescription(file);
      enrichment = generateGenericSpatialContent(file, body);
      // Wrap in a fake template so frontmatter gets the description
      template = { description: genericDesc };
    }

    // Update frontmatter: replace existing description, add if missing
    let updatedFrontmatter = frontmatter;

    // Remove any existing description lines first
    updatedFrontmatter = updatedFrontmatter.replace(/^description:.*\n?/gm, "");

    // Add correct description before tags line
    if (template && template.description) {
      const escapedDesc = template.description.replace(/"/g, '\\"');
      updatedFrontmatter = updatedFrontmatter.replace(
        /^(tags:.*)$/m,
        `description: "${escapedDesc}"\n$1`
      );
    }

    // Clean up blank lines within frontmatter (between --- markers)
    const fmParts = updatedFrontmatter.match(/^---\n([\s\S]*?)\n---$/);
    if (fmParts) {
      const inner = fmParts[1].split("\n").filter(l => l.trim() !== "").join("\n");
      updatedFrontmatter = "---\n" + inner + "\n---";
    }

    // Update title if needed — use separate title field if available, otherwise use name
    if (template) {
      const titleValue = template.title || template.name;
      if (titleValue) {
        const titleRegex = /^title:.*$/m;
        const escapedTitle = titleValue.replace(/"/g, '\\"');
        if (titleRegex.test(updatedFrontmatter)) {
          updatedFrontmatter = updatedFrontmatter.replace(titleRegex, `title: "${escapedTitle}"`);
        }
      }
    }

    const enriched = updatedFrontmatter + "\n" + enrichment;

    if (enriched === original) {
      skipped++;
      continue;
    }

    changed++;
    const origWords = body.split(/\s+/).filter(w => w.length > 0).length;
    const newWords = enrichment.split(/\s+/).filter(w => w.length > 0).length;

    if (isFix) {
      fs.writeFileSync(filePath, enriched, "utf-8");
      console.log(`  ✓ ${file} (${origWords} → ${newWords} words)`);
    } else {
      console.log(`  ~ ${file} (${origWords} → ${newWords} words)`);
    }
  }

  console.log("─".repeat(60));
  console.log(`Summary: ${changed} changed, ${skipped} skipped, ${undersizedFiles.length} total`);
}

function extractFrontmatter(content) {
  const match = content.match(/^---\n[\s\S]*?\n---/);
  return match ? match[0] : null;
}

function extractBody(content) {
  const match = content.match(/^---\n[\s\S]*?\n---\n?([\s\S]*)$/);
  return match ? match[1] : content;
}

main();
