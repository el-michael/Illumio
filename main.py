import csv

# Global variables regarding files
LOOKUP_TABLE_FILE = "lookup_table.csv"
FLOW_LOGS_FILE = "flow_logs.txt"
OUTPUT_FILE = "output.txt"

# Hashmap of needed protocol numbers
# Add additional protocols as needed (maybe have an automated system to do this in the future)
protocol_numbers = {
    "1" : "icmp",
    "6" : "tcp",
    "17" : "udp"
}

# Function that reads the lookup_table and parses the data
# returns a hashmap containing "(dst_port, protocol) : tag"
def read_csv_file(filename):
    tags_dict = {}
    with open(filename, "r") as file:
        csv_file = csv.reader(file)
        # Skip the header so it's not in our tag's hashmap
        next(csv_file)
        # Map data with in this format -> (dst_port, protocol) : tag
        for line in csv_file:
            dst_port, protocol, tag = line[0], line[1].lower(), line[2].lower()
            tags_dict[(dst_port, protocol)] = tag
    return tags_dict

# Function that processes the given flow_logs data and counts the number of matches given the tags hashmap
# Processing logs is only sustainable for mapping (dst_port, protocol) : tag.
# Also only flow logs records version 2 is supportable
# Returns a dictionary of amount of tags counted and comboinations made
def process_flow_logs(filename, tags_dict):
    tag_counts = {}
    combo_counts = {}
    with open(filename, "r") as file:
        for entry, line in enumerate(file):
            fields = line.split()
            # Default formatting of flow log records is only 14. Version 2 is only support.
            # Ensure that dst_port and protocol number exists
            if len(fields) < 14 or fields[0] != "2" or fields[6] == "-" or fields[7] == "-":
                print(f"Entry {entry} is invalid")
                continue
            # Extract the data neccessary to compare with the tags hashmap
            dst_port, protocol = fields[6], protocol_numbers[fields[7]]
            data, combo = (dst_port, protocol), f"{dst_port},{protocol}"
            tag = tags_dict.get(data)

            # Count the number of matches
            if tag:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            else:
                tag_counts["Untagged"] = tag_counts.get("Untagged", 0) + 1
            combo_counts[combo] = combo_counts.get(combo, 0) + 1

    return tag_counts, combo_counts

# Function that prints the output in expected format
def print_output(filename, tag_counts, combo_counts):
    with open(filename, "w") as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for key, value in tag_counts.items():
            file.write(f"{key}, {value}\n")

        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for key, value in combo_counts.items():
            file.write(f"{key},{value}\n")

def main():
    tags_dict = read_csv_file(LOOKUP_TABLE_FILE)
    tag_counts, combo_counts = process_flow_logs(FLOW_LOGS_FILE, tags_dict)
    print_output(OUTPUT_FILE, tag_counts, combo_counts)

main()